# 🩺 Diabetes Prediction API & Web App

🚀 **Live Demo (Streamlit UI):**
👉https://diabetes-flask-api-7nd9dyskwt45neckqklsv5.streamlit.app/

🌐 **Live API (Flask - Render):**
👉 https://diabetes-api-mleu.onrender.com

---

## 📌 Project Overview

This project predicts whether a person is diabetic or not using Machine Learning.

It includes:

* 🔹 Flask API for prediction
* 🔹 Streamlit UI for user interaction
* 🔹 Deployed on Render (API) + Streamlit Cloud (Frontend)

---

## ⚙️ Tech Stack

* Python
* Scikit-learn
* Flask
* Streamlit
* NumPy

---

## 🔮 How It Works

1. User enters input values in Streamlit UI
2. Data is sent to Flask API (`/predict`)
3. Model processes input
4. Prediction is returned and displayed

---

## 📡 API Endpoint

POST `/predict`

Example JSON:

```json
{
  "pregnancies": 2,
  "glucose": 120,
  "blood_pressure": 70,
  "skin_thickness": 20,
  "insulin": 85,
  "bmi": 30.5,
  "dpf": 0.5,
  "age": 25
}
```

Response:

```json
{
  "prediction": "0"
}
```

---

## 📂 Project Structure

* `app.py` → Flask API
* `streamlit_app.py` → UI
* `model.pkl` → Trained model
* `requirements.txt` → Dependencies

---

## 💡 Future Improvements

* Add authentication
* Improve UI design
* Deploy using Docker

---
