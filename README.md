# 🌦️ Climate Intelligence & Weather Forecasting System
### Advanced Weather Analytics, Machine Learning & Climate Risk Assessment

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![Flask](https://img.shields.io/badge/Flask-Web_Framework-black?logo=flask)
![Machine Learning](https://img.shields.io/badge/Machine_Learning-Scikit--Learn-orange)
![Pandas](https://img.shields.io/badge/Data_Analysis-Pandas-150458?logo=pandas)
![Status](https://img.shields.io/badge/Project-Academic_Mini_Project-success)

**Climate Intelligence & Weather Forecasting System** is a Python-based web application designed to analyze weather patterns, forecast future temperature and rainfall probabilities, and study long-term climate trends using Machine Learning.

The system combines data analytics, predictive modeling and interactive weather visualizations to help users understand changing weather conditions and potential climate-related risks.

---

## 🌍 Project Overview

Weather conditions and climate patterns are changing over time. Rising temperatures, irregular rainfall and extreme weather events can create serious challenges for agriculture, public health, water resources and the environment.

This project uses historical weather data and Machine Learning techniques to:

- Forecast daily average temperature for the next 7 days.
- Estimate the probability of rainfall.
- Analyze long-term temperature trends.
- Study seasonal weather patterns.
- Compare rainfall and temperature variations.
- Evaluate Machine Learning model performance.
- Improve awareness of climate-related risks.

## 🎯 Project Objectives

1. Analyze historical weather datasets using Python.
2. Develop predictive models for temperature forecasting.
3. Estimate rainfall probability using classification algorithms.
4. Identify long-term warming trends and seasonal variations.
5. Visualize weather patterns through graphical representations.
6. Evaluate prediction accuracy using statistical metrics.
7. Build a user-friendly web application for weather analytics.

---

## 🚀 Key Features

| Module | Features |
|---|---|
| Dashboard | Weather summary, 7-day forecast and historical charts |
| Weather Forecast | Daily temperature and rainfall probability |
| Forecast Analysis | Date selection and historical backtesting |
| User Readings | Custom weather input and future predictions |
| Climate Trends | Annual warming trend and seasonal analysis |
| Rainfall Analysis | Rainfall totals and distribution |
| Model Performance | Model comparison and evaluation metrics |
| Feature Importance | Identify influential weather variables |
| REST API | Forecast and application health endpoints |

## 🧠 Machine Learning Algorithms

The project uses the following algorithms:

**1. Linear Regression**
- Predicts future average temperature.
- Establishes a baseline regression model.

**2. Random Forest**
- Handles nonlinear weather relationships.
- Used for temperature forecasting and rainfall classification.

**3. Gradient Boosting**
- Combines multiple decision trees.
- Used for predictive model comparison.

**Baseline Models**
- Persistence forecasting.
- Climatology-based forecasting.

### Prediction Targets

- Average temperature (°C).
- Rainfall probability (%).
- Seven forecasting horizons (1–7 days).

---

## 📊 Data Analytics & Visualization

The system analyzes:

- Daily maximum and minimum temperatures.
- Average temperature variations.
- Humidity patterns.
- Rainfall distribution.
- Wind speed changes.
- Atmospheric pressure.
- Seasonal and annual climate trends.

Visualizations help identify relationships between weather variables and changing climate patterns.

---

## 🛠️ Technology Stack

| Technology | Purpose |
|---|---|
| Python | Core programming |
| NumPy | Numerical computation |
| Pandas | Data processing |
| Scikit-learn | Machine Learning |
| Matplotlib | Data visualization |
| Flask | Web application |
| HTML5 | Frontend structure |
| CSS3 | Interface styling |
| JavaScript | Frontend interactions |
| CSV | Dataset storage |

---

## 📁 Project Structure

```text
climate-risk-analytics/
│
├── app.py
├── weather_core.py
├── charts.py
├── train.py
├── data_generator.py
├── requirements.txt
│
├── data/
│   └── weather_data.csv
│
├── models/
│   └── weather_models.joblib
│
├── templates/
│   ├── dashboard.html
│   ├── forecast.html
│   ├── climate_trends.html
│   └── ...
│
├── static/
│   └── style.css
│
└── tests/
    └── test_project.py
```

---

## ⚙️ Installation & Setup

### Step 1: Clone Repository

```bash
git clone https://github.com/IbrahimAnsari93/Weather-Data-Analysis.git
```

### Step 2: Navigate to Project

```bash
cd Weather-Data-Analysis
```

### Step 3: Create Virtual Environment

```bash
python -m venv .venv
```

### Step 4: Activate Environment

**Windows:**

```bash
.venv\Scripts\activate
```

### Step 5: Install Dependencies

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### Step 6: Run Application

```bash
python app.py
```

### Step 7: Open in Browser

```text
http://127.0.0.1:5000
```

---

## 📈 Model Evaluation

The project evaluates temperature forecasting models using:

| Metric | Purpose |
|---|---|
| MAE | Mean Absolute Error |
| RMSE | Root Mean Squared Error |
| R² Score | Explained variance |

Rainfall classification is evaluated using:

- Accuracy
- Precision
- Recall
- F1 Score
- ROC-AUC

A time-ordered training and testing split is used to preserve chronological order and avoid future-data leakage.

---

## 🔌 API Endpoints

### Weather Forecast API

```http
GET /api/forecast?date=YYYY-MM-DD
```

Returns the seven-day weather forecast for the requested date.

### Application Health API

```http
GET /api/health
```

Returns application health information.

---

## 🧪 Testing

Run automated unit tests:

```bash
python -m unittest discover -s tests -v
```

The existing test suite contains 17 automated tests.

---

## 🌱 Climate Awareness & Environmental Importance

Climate analysis is important for understanding environmental changes and their potential consequences.

This project demonstrates how weather analytics can help study:

- Increasing temperature patterns.
- Irregular rainfall distribution.
- Seasonal weather variations.
- Potential heatwave conditions.
- Rainfall-related environmental challenges.
- Long-term climate variability.

**Our vision:** Transform weather data into meaningful information that encourages environmental awareness and better climate-related decision-making.

---

## ⚠️ Dataset Disclaimer

The bundled dataset is synthetic and represents a central-India-style climate pattern for demonstration and educational purposes.

It should not be treated as verified historical meteorological observations or scientific evidence of actual climate change.

For real-world analysis, the system supports a CSV dataset with the following columns:

```text
date
temp_max
temp_min
humidity
rainfall
wind_speed
pressure
```

Supported potential data sources include Open-Meteo, NASA POWER and verified meteorological datasets.

---

## 🔮 Future Enhancements

The following features are proposed for future development:

- Real-time weather API integration.
- Interactive India weather map.
- Advanced climate risk monitoring.
- Heatwave and extreme rainfall alerts.
- Admin authentication and role management.
- SQL database integration.
- Interactive Plotly dashboards.
- PDF climate analysis reports.
- Cloud deployment.
- Advanced time-series forecasting models.

---

## 👨‍💻 Developer

**Ibrahim Ansari**

B.Tech – Computer Science & Engineering (AI & ML)

**Project:** Climate Intelligence & Weather Forecasting System

**GitHub:** [IbrahimAnsari93](https://github.com/IbrahimAnsari93)

**Repository:** [Weather-Data-Analysis](https://github.com/IbrahimAnsari93/Weather-Data-Analysis)

---

## 📜 Project Information

- Project Type: Academic Minor Project
- Domain: Data Analytics & Machine Learning
- Application: Weather Forecasting & Climate Analysis
- Programming Language: Python
- Framework: Flask

---

### 🌍 Turning Weather Data into Climate Intelligence.

*Understand the weather. Analyze the climate. Prepare for the future.*