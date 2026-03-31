import requests

url = "https://diabetes-api-mleu.onrender.com/predict"

data = {
    "pregnancies": 2,
    "glucose": 130,
    "blood_pressure": 80,
    "skin_thickness": 20,
    "insulin": 85,
    "bmi": 28.5,
    "dpf": 0.5,
    "age": 30
}

response = requests.post(url, json=data)

print(response.json())