# AQI Tracker — AI-Powered Air Quality & Weather Forecasting

> An AI-powered platform that predicts real-time Air Quality Index (AQI) and weather conditions for Indian cities using Random Forest Regression.

---

## 📌 Overview

Air pollution tracking today suffers from limited real-time data integration, poor forecasting accuracy, and a lack of accessible, user-friendly tools. **AQI Tracker** solves this by combining live API data with historical trends to forecast AQI and weather conditions, presenting results through an interactive, visually engaging dashboard.

**Team:** Mini Project — Third Year Engineering, CSE (Data Science)
- Sharayu Mahajan (22107051)
- Kalpana Mohanty (22107059)
- Rishi Mane (22107063)
- Avadhoot Virkar (22107064)

**Project Guide:** Ms. Dipali Gat
**Institute:** A.P. Shah Institute of Technology, University of Mumbai (Academic Year 2024–25)

---

## ❗ Problem This Solves

- Existing AQI systems rely on historical data alone, without incorporating real-time meteorological variables (wind speed, humidity, temperature) that significantly affect AQI values
- Traditional AQI computation methods struggle to adapt to rapidly changing pollution dynamics
- Lack of integration with real-time APIs and IoT-enabled sensors limits responsiveness
- No accessible, personalized, alert-based system for everyday users to track pollution exposure

## 🎯 Objectives

- Predict real-time AQI for Indian cities using live API data and machine learning
- Integrate weather forecasting alongside AQI data for a complete environmental overview
- Classify AQI levels (Good, Moderate, Unhealthy, etc.) and send alerts when safety thresholds are crossed
- Visualize historical and real-time trends through an interactive dashboard
- Achieve high forecasting accuracy through continuous model improvement

---

## 🧠 Model Used & Performance

Two models were evaluated for AQI/weather forecasting:

**Random Forest Regressor** — an ensemble of decision trees that averages predictions to improve accuracy and reduce overfitting. *(Selected as the final model.)*

**FB Prophet** — Facebook's open-source time-series forecasting tool, good at detecting trends and seasonality but less effective here on complex, multi-feature environmental data.

**Final results:**

```
Random Forest Regressor accuracy:   85%
FB Prophet accuracy:                60%
R² Score (Random Forest):           ~0.98 (strong model fit)
Mean Squared Error (Random Forest): Low

Accuracy share when compared head-to-head:
  Random Forest: 58.6%
  FB Prophet:    41.4%
```

Random Forest Regression was selected for final implementation due to its superior accuracy, stability across temperature/humidity/AQI parameters, and lower error rate compared to FB Prophet.

---

## 🛠️ Technology Stack

**Frontend:**
- HTML5, CSS3

**Backend:**
- Python
- Flask
- Pandas, NumPy
- Scikit-learn (Random Forest Regressor)
- Matplotlib (data visualization)

**Data:**
- Kaggle datasets (historical AQI & weather data)
- Live weather/AQI API integration

---

## ⚙️ How It Works

1. **Load Historical Data** — The system loads previously collected and trained AQI and weather datasets.
2. **Preprocess Data** — Historical data is cleaned and formatted for consistency (handling missing/noisy values via imputation and smoothing).
3. **Fetch Live Data (API)** — Real-time weather and pollution data is pulled from an external API.
4. **Train on Combined Data** — Live and historical data are merged to build a robust training set.
5. **Predict Future Trends** — The Random Forest model forecasts AQI and weather trends up to 12 months ahead.
6. **Analyze & Visualize** — Results are rendered as line graphs, bar charts, and scatter plots for interpretability.
7. **User Interaction** — Users select a city, view current AQI/weather, and receive classified alerts (Good, Moderate, Unhealthy, Hazardous) when safety thresholds are exceeded.

---

## 🏗️ System Architecture

<img width="751" height="388" alt="image" src="https://github.com/user-attachments/assets/79fd55cd-c805-4b85-99ca-37b8195cf7fd" />




---

## 📸 Screenshots

<!-- Paste each screenshot below its heading -->

### Home Page
<img width="1028" height="484" alt="image" src="https://github.com/user-attachments/assets/bd488556-b9f6-424a-a475-b4203fcdc503" />


### Weather Prediction Dashboard
<img width="986" height="484" alt="image" src="https://github.com/user-attachments/assets/07907330-d6cf-4b90-a966-5bdafab60519" />


### Air Quality Index Page
<img width="1004" height="433" alt="image" src="https://github.com/user-attachments/assets/313eb878-0bb9-4d5c-9e1e-bb92c8af4ccc" />


### Prediction Graphs (Line, Bar, Scatter)
<img width="1004" height="425" alt="image" src="https://github.com/user-attachments/assets/cd6d0852-5767-4450-aa25-3d2f80978220" />


---

## 🚀 Getting Started

```bash
# Clone the repository
git clone https://github.com/elfeyaoo/My-Projects.git
cd My-Projects/AQI-Tracker

# Create a virtual environment
python -m venv venv
source venv/bin/activate      # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Set up your weather/AQI API key in a .env file
# API_KEY=your_api_key_here

# Run the application
flask run
```
*(Adjust these commands to match your actual project structure, and add a `requirements.txt` if you haven't already — this makes the repo runnable for anyone who clones it, including recruiters.)*

---

## 📊 Key Insights

- Random Forest Regressor showed higher and more stable accuracy across temperature, humidity, and AQI parameters compared to FB Prophet
- FB Prophet was useful for trend/seasonality visualization but less accurate in this multi-feature environment
- Interpolation and imputation techniques successfully addressed incomplete AQI readings and missing weather values

---

## 🔮 Future Scope

- Deploy models as APIs for real-time prediction updates
- Add geo-spatial insights with city-wise AQI heatmaps
- Explore hybrid models combining LSTM (deep learning) with ensemble methods for improved accuracy
- Integrate real-time traffic pollution monitoring and wearable health device data
- Build a mobile app with push notifications and location-based alerts
- Integrate IoT-enabled low-cost air sensors for hyper-local AQI readings

---


## 📄 License

*(Add a license if you intend for others to reuse this code — MIT is a common choice for student/portfolio projects.)*
