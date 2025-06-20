
import streamlit as st
import pandas as pd
import numpy as np
import joblib

from sklearn.ensemble import RandomForestClassifier

st.set_page_config(page_title="Patient No-Show Predictor", layout="wide")

st.title("📅 Smart Scheduling: Patient No-Show Prediction")

st.markdown("Use this tool to predict whether a patient is likely to miss their medical appointment and plan overbooking accordingly.")

# Sidebar Inputs
st.sidebar.header("Patient Details")
gender = st.sidebar.selectbox("Gender", ["Female", "Male"])
age = st.sidebar.slider("Age", 0, 100, 30)
scholarship = st.sidebar.checkbox("Enrolled in Welfare Program (Scholarship)")
hypertension = st.sidebar.checkbox("Has Hypertension")
diabetes = st.sidebar.checkbox("Has Diabetes")
alcoholism = st.sidebar.checkbox("Has Alcoholism")
handicap = st.sidebar.checkbox("Has Handicap")
sms_received = st.sidebar.checkbox("Received SMS Reminder")
lead_time = st.sidebar.slider("Days Between Scheduling and Appointment", 0, 100, 5)
weekday = st.sidebar.selectbox("Appointment Day of the Week", ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"])
hour_scheduled = st.sidebar.slider("Hour Scheduled (24H)", 0, 23, 10)

# Feature mapping
gender_val = 0 if gender == "Female" else 1
weekday_map = {'Monday': 0, 'Tuesday': 1, 'Wednesday': 2, 'Thursday': 3, 'Friday': 4, 'Saturday': 5}
weekday_val = weekday_map[weekday]

# Input DataFrame
input_df = pd.DataFrame([{
    'Gender': gender_val,
    'Age': age,
    'Scholarship': scholarship,
    'Hypertension': hypertension,
    'Diabetes': diabetes,
    'Alcoholism': alcoholism,
    'Handicap': handicap,
    'SMS_received': sms_received,
    'LeadTime': lead_time,
    'AppointmentWeekday': weekday_val,
    'HourScheduled': hour_scheduled
}])

# Load or simulate model
@st.cache_resource
def load_model():
    try:
        return joblib.load("random_forest_noshow_model.pkl")
    except:
        model = RandomForestClassifier()
        model.fit(np.random.rand(100, 11), np.random.randint(0, 2, size=100))  # Dummy fallback
        return model

model = load_model()

# Predict show-up probability
show_prob = model.predict_proba(input_df)[0][1]

# Output
st.subheader("Prediction Result")
st.metric("Predicted Show-Up Probability", f"{show_prob:.2%}")

if show_prob < 0.5:
    st.error("⚠️ This patient is at HIGH risk of no-show. Consider overbooking.")
else:
    st.success("✅ This patient is likely to show up.")

# Footer
st.markdown("---")
st.caption("Built with ❤️ using Streamlit · Predict & optimize hospital schedules")
