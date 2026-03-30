import requests

url = "http://127.0.0.1:5000/predict"

data = {
    "pregnancies": 2,
    "glucose": 140,
    "blood_pressure": 80,
    "skin_thickness": 20,
    "insulin": 85,
    "bmi": 32,
    "dpf": 0.5,
    "age": 45
}

response = requests.post(url, json=data)

print(response.json())