# Patient No-Show Predictor & Overbooking Optimizer

This project predicts whether a patient will show up for a scheduled medical appointment using historical data. It also simulates overbooking strategies to help hospitals optimize time slots and reduce operational inefficiencies.

---

## 📊 Problem Statement

Medical appointment no-shows lead to underutilized resources and financial losses. By predicting which patients are at high risk of not showing up, hospitals can implement overbooking strategies to fill potential gaps.

---

## 📁 Dataset

* **Source**: [Kaggle - Medical Appointment No Shows](https://www.kaggle.com/datasets/joniarroba/noshowappointments)
* **Records**: 110,000+ appointments
* **Features**:

  * `Gender`, `Age`, `Neighbourhood`
  * `Hypertension`, `Diabetes`, `Alcoholism`, `SMS_received`
  * `ScheduledDay`, `AppointmentDay`
  * `No-show` (Target variable)

---

## 🔧 Project Structure

```
├── data/
│   └── healthcare_noshows_appt.csv
├── notebooks/
│   ├── 02_eda_visualization.ipynb
│   ├── 03_modeling_prediction.ipynb
│   ├── 03_modeling_prediction_balanced.ipynb
│   └── 04_overbooking_simulation.ipynb
├── app/
│   ├── streamlit_app.py
│   └── random_forest_noshow_model.pkl
├── requirements.txt
└── README.md
```

---

## 🔍 EDA Highlights

* Patients aged 0–20 are more likely to miss appointments.
* Long wait time between scheduling and appointment increases no-show likelihood.
* Receiving an SMS reminder does not strongly affect attendance.

---

## 🧠 Modeling

* **Models tried**:

  * Logistic Regression
  * Random Forest ✅ *(Best performance)*
  * XGBoost
* **Metrics used**:

  * Accuracy, F1-score, Recall, Confusion Matrix
* **Handling Imbalance**: Oversampling techniques applied in `03_modeling_prediction_balanced.ipynb`

---

## 🔎 Explainability

* SHAP used to interpret the Random Forest model.
* Key factors influencing predictions:

  * `days_until_appointment`
  * `age`
  * `hypertension`, `alcoholism`, `diabetes`

---

## 📈 Overbooking Simulation

* Simulated doubling up appointments for high-risk no-show patients.
* Metrics observed:

  * Idle slots reduced
  * Crowd control maintained
* Strategy effective when applied with precision to top 10–15% risk group.

---

## 🌐 Streamlit App

Run locally:

```bash
streamlit run app/streamlit_app.py
```

Features:

* Upload test data
* Predict no-show risk
* Simulate overbooking logic

---

## ☁️ Deploy to Streamlit Cloud

1. Push project to GitHub
2. Sign in to [Streamlit Cloud](https://streamlit.io/cloud)
3. Click `New app` > Connect to GitHub repo
4. Set file path to `app/streamlit_app.py`
5. Click `Deploy`

---

## 📦 Requirements

Install dependencies with:

```bash
pip install -r requirements.txt
```

---

## 🧠 Author & Contact

**Sandeep Undurthi**
M.S. in Computer Science @ Utah State University
Email: \[[your.email@example.com](mailto:your.email@example.com)]
GitHub: [github.com/yourusername](https://github.com/yourusername)

---

## 📌 License

MIT License
