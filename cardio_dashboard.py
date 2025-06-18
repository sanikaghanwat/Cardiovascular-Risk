import streamlit as st
import joblib
import numpy as np
import base64

# ---------- Background Function ----------
def set_background(image_file):
    with open(image_file, "rb") as img_file:
        encoded_string = base64.b64encode(img_file.read()).decode()

    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/jpg;base64,{encoded_string}");
            background-size: cover;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }}

        /* Make all form labels bold and black */
        label, div[data-baseweb="select"] > div, .css-1cpxqw2 {{
            font-weight: bold !important;
            color: black !important;
        }}

        /* Input values (inside number boxes, dropdowns) */
        input, select, textarea {{
            font-weight: bold !important;
            color: black !important;
        }}

        /* Make the dropdown selected text also bold */
        .css-1jqq78o-placeholder {{
            font-weight: bold !important;
            color: black !important;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

set_background("background.jpg")

# ---------- Load Model ----------
model = joblib.load("cardio_model.pkl")

# ---------- Title and Icon ----------
col1, col2 = st.columns([2, 10])
with col1:
    st.image("heart_icon.jpg", width=120)
with col2:
    st.title("Cardio Disease Risk Prediction Dashboard")

# ---------- Inputs ----------
age = st.number_input("Age", min_value=1, max_value=120)
sex_display = st.selectbox("Sex", options=["Female", "Male"])
sex = 0 if sex_display == "Female" else 1

cigsPerDay = st.number_input("Cigarettes Per Day", min_value=0)
BPMeds_display = st.selectbox("On Blood Pressure Meds?", options=["No", "Yes"])
BPMeds = 1 if BPMeds_display == "Yes" else 0

prevalentStroke_display = st.selectbox("History of Stroke?", options=["No", "Yes"])
prevalentStroke = 1 if prevalentStroke_display == "Yes" else 0

totChol = st.number_input("Total Cholesterol", min_value=100)
diaBP = st.number_input("Diastolic BP", min_value=40)
BMI = st.number_input("BMI", min_value=10.0)
heartRate = st.number_input("Heart Rate", min_value=40)
glucose = st.number_input("Glucose Level", min_value=50)

# ---------- Prediction ----------
if st.button("Predict Cardio Risk"):
    features = np.array([[age, sex, cigsPerDay, BPMeds, prevalentStroke,
                          totChol, diaBP, BMI, heartRate, glucose]])
    
    prediction = model.predict(features)[0]

    if prediction == 1:
        st.error("⚠️ High Risk of Cardio Disease")
    else:
        st.success("✅ Low Risk of Cardio Disease")
