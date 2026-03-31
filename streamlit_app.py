import streamlit as st
import requests

st.title("Diabetes Prediction App")

pregnancies = st.number_input("Pregnancies")
glucose = st.number_input("Glucose")
blood_pressure = st.number_input("Blood Pressure")
skin_thickness = st.number_input("Skin Thickness")
insulin = st.number_input("Insulin")
bmi = st.number_input("BMI")
dpf = st.number_input("Diabetes Pedigree Function")
age = st.number_input("Age")

if st.button("Predict"):
    url = "https://diabetes-api-mleu.onrender.com/predict"

    data = {
        "pregnancies": pregnancies,
        "glucose": glucose,
        "blood_pressure": blood_pressure,
        "skin_thickness": skin_thickness,
        "insulin": insulin,
        "bmi": bmi,
        "dpf": dpf,
        "age": age
    }

    response = requests.post(url, json=data)

    if response.status_code == 200:
        result = response.json()["prediction"]
        st.success(f"Prediction: {result}")
    else:
        st.error("Error connecting to API")