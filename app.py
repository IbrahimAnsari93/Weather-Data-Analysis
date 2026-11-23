
"""Flask web app: Climate Risk Analytics and Weather Forecasting.
Run: python app.py
"""

from pathlib import Path

import pandas as pd
from flask import Flask, jsonify, render_template, request

import charts
from weather_core import (
    FIELDS,
    annual_summary,
    build_features,
    features_from_observation,
    forecast,
    get_artifacts,
    load_data,
    monthly_climatology,
    temperature_trend,
    validate_observation,
)

BASE = Path(__file__).parent

# Maximum date allowed in the forecast calendar
MAX_FORECAST_DATE = pd.Timestamp("2035-12-31")


def create_app(data_path=None, model_path=None, fast=False):

    app = Flask(__name__)

    # Load weather dataset and ML models
    df = load_data(data_path or BASE / "data" / "weather_data.csv")

    art = get_artifacts(
        df,
        model_path or BASE / "models" / "weather_models.joblib",
        fast=fast
    )

    feats = build_features(df).dropna()

    annual = annual_summary(df)
    trend = temperature_trend(annual)
    monthly = monthly_climatology(df)

    split_date = pd.Timestamp(art["split_date"])
    last = df.index[-1]

    cache = {}

    def cached(key, fn):
        if key not in cache:
            cache[key] = fn()
        return cache[key]

    # --------------------------------------------------
    # DATE VALIDATION: 2024 TO 2035
    # --------------------------------------------------

    def parse_date(raw):

        try:
            d = pd.Timestamp(str(raw).strip()).normalize()

        except Exception:
            return None

        min_date = feats.index[0]

        if min_date <= d <= MAX_FORECAST_DATE:
            return d

        return None

    date_range_msg = (
        f"Pick a date between {feats.index[0].date()} "
        f"and {MAX_FORECAST_DATE.date()}."
    )

    # --------------------------------------------------
    # FORECAST ENGINE
    # --------------------------------------------------

    def run_forecast(date):

        date = pd.Timestamp(date).normalize()

        # Historical dates: use actual dataset features
        if date in feats.index:

            X = feats.loc[[date]]

        # Future dates: use latest available observation
        else:

            latest_observation = df.iloc[-1].to_dict()

            X = features_from_observation(
                latest_observation,
                date
            )

        # Generate 7-day forecast
        fc = forecast(art, X, date)

        # Add actual values wherever available
        for f in fc:

            forecast_date = pd.Timestamp(f["date"])

            if forecast_date in df.index:

                f["actual_temp"] = float(
                    df.loc[forecast_date, "temp_avg"]
                )

                f["actual_rain"] = float(
                    df.loc[forecast_date, "rainfall"]
                )

                f["error"] = round(
                    f["temp"] - f["actual_temp"], 1
                )

        return fc

    # --------------------------------------------------
    # HOME PAGE
    # --------------------------------------------------

    @app.route("/")
    def index():

        return render_template(
            "index.html",
            fc=run_forecast(last),
            today=df.iloc[-1],
            last=last.date(),
            chart=cached(
                "history",
                lambda: charts.history_chart(df)
            ),
            n_days=len(df),
            art=art,
            start=df.index[0].date(),
            page="home"
        )

    # --------------------------------------------------
    # FORECAST PAGE
    # --------------------------------------------------

    @app.route("/forecast")
    def forecast_page():

        raw = request.args.get("date")

        error = None
        date = last

        if raw:

            parsed = parse_date(raw)

            if parsed is None:

                error = (
                    f"'{raw}' is not a usable date. "
                    f"{date_range_msg}"
                )

            else:

                date = parsed

        fc = run_forecast(date)

        # Differentiate historical test dates and future projections
        is_future = date > last
        unseen = last >= date >= split_date

        if is_future:
            forecast_status = "Future experimental projection"
        elif unseen:
            forecast_status = "Historical test period"
        else:
            forecast_status = "Historical training period"

        # Only pass actual observation for historical dates
        obs = df.loc[date] if date in df.index else None

        return render_template(
            "forecast.html",
            fc=fc,
            date=date.date(),
            error=error,
            page="forecast",
            chart=charts.forecast_chart(df, date, fc),
            unseen=unseen,
            is_future=is_future,
            forecast_status=forecast_status,
            split=art["split_date"],
            dmin=feats.index[0].date(),
            dmax=MAX_FORECAST_DATE.date(),
            obs=obs,
        ), (400 if error else 200)

    # --------------------------------------------------
    # CUSTOM FORECAST PAGE
    # --------------------------------------------------

    @app.route("/custom", methods=["GET", "POST"])
    def custom():

        errors = []
        fc = None
        chart = None

        form = {
            k: round(float(df.iloc[-1][k]), 1)
            for k in FIELDS
        }

        form["date"] = str(last.date())

        if request.method == "POST":

            form = request.form.to_dict()

            obs, date, errors = validate_observation(
                request.form
            )

            if not errors:

                fc = forecast(
                    art,
                    features_from_observation(obs, date),
                    date
                )

                chart = charts.forecast_chart(
                    df,
                    pd.Timestamp("1900-01-01"),
                    fc
                )

        return render_template(
            "custom.html",
            fc=fc,
            chart=chart,
            errors=errors,
            form=form,
            fields=FIELDS,
            page="custom"
        ), (400 if errors else 200)

    # --------------------------------------------------
    # CLIMATE ANALYSIS
    # --------------------------------------------------

    @app.route("/climate")
    def climate():

        return render_template(
            "climate.html",
            trend=trend,
            annual=annual,
            page="climate",
            c_trend=cached(
                "c_trend",
                lambda: charts.annual_trend_chart(annual, trend)
            ),
            c_clim=cached(
                "c_clim",
                lambda: charts.climatograph(monthly)
            ),
            c_rain=cached(
                "c_rain",
                lambda: charts.annual_rain_chart(annual)
            )
        )

    # --------------------------------------------------
    # MACHINE LEARNING MODELS
    # --------------------------------------------------

    @app.route("/models")
    def models():

        return render_template(
            "models.html",
            art=art,
            page="models",
            c_cmp=cached(
                "m1",
                lambda: charts.model_compare_chart(
                    art["comparison"]
                )
            ),
            c_pa=cached(
                "m2",
                lambda: charts.pred_actual_chart(
                    art["test_pred"]
                )
            ),
            c_imp=cached(
                "m3",
                lambda: charts.importance_chart(
                    art["importance"]
                )
            ),
            c_hor=cached(
                "m4",
                lambda: charts.horizon_chart(
                    art["horizon_metrics"]
                )
            )
        )

    # --------------------------------------------------
    # ABOUT PAGE
    # --------------------------------------------------

    @app.route("/about")
    def about():

        return render_template(
            "about.html",
            page="about",
            art=art,
            n_days=len(df),
            start=df.index[0].date(),
            end=last.date()
        )

    # --------------------------------------------------
    # FORECAST API
    # --------------------------------------------------

    @app.route("/api/forecast")
    def api_forecast():

        raw = request.args.get("date")

        date = last if not raw else parse_date(raw)

        if date is None:

            return jsonify({
                "error": f"Invalid date. {date_range_msg}"
            }), 400

        return jsonify({
            "origin_date": str(date.date()),
            "model": art["best_model"],
            "forecast": run_forecast(date),
            "forecast_type": (
                "experimental_future_projection"
                if date > last
                else "historical_data_forecast"
            )
        })


    @app.route("/api/health")
    def health():

        return jsonify({
            "status": "ok",
            "best_model": art["best_model"],
            "rows": len(df),
            "historical_start": str(df.index[0].date()),
            "historical_end": str(last.date()),
            "maximum_forecast_date": str(
                MAX_FORECAST_DATE.date()
            )
        })

    @app.errorhandler(404)
    def not_found(_):

        return render_template(
            "error.html",
            message="Page not found.",
            page=""
        ), 404

    return app


if __name__ == "__main__":

    create_app().run(
        host="127.0.0.1",
        port=5000,
        debug=False
    )
