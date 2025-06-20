# 🧠 Smart Scheduling: Patient No-Show Predictor

An end-to-end machine learning and Streamlit project that predicts patient no-shows for medical appointments and supports overbooking strategies in hospital scheduling.

## 📁 Project Structure
```
patient-no-show-predictor/
├── data/                        # Input dataset
├── notebooks/                  # Jupyter notebooks for data cleaning, EDA, modeling
├── app/                        # Streamlit web app + model
├── screenshots/                # (Add your app screenshots here)
├── requirements.txt            # Install dependencies
└── README.md                   # Project overview
```

## 🚀 Features
- Predicts likelihood of patient no-shows using Random Forest
- Class balancing using SMOTE for fairer model performance
- Visual EDA with gender, age, and weekday trends
- Overbooking simulation for high-risk time slots
- Interactive Streamlit app with SHAP explainability

## 📈 Run Locally

```bash
pip install -r requirements.txt
streamlit run app/streamlit_app.py
```

## 📊 Notebooks Included
- `01_data_cleaning.ipynb` – Feature engineering and cleaning
- `02_eda_visualization.ipynb` – Exploratory data analysis
- `03_modeling_prediction.ipynb` – Base model training
- `03_modeling_prediction_balanced.ipynb` – Balanced classification
- `04_overbooking_simulation.ipynb` – Risk-based overbooking logic

## 🌐 Streamlit App Screenshot
_Add a screenshot in `/screenshots/` and link it here._

---
Built with ❤️ using Streamlit · Predict & optimize hospital schedules
