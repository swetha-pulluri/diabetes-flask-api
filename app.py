from flask import Flask, request, jsonify
import pickle
import os

app = Flask(__name__)

# Load trained model
model = pickle.load(open("model.pkl", "rb"))

@app.route("/")
def home():
    return "Diabetes API Running"

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json

    # prepare input in correct order
    input_data = [[
        data["pregnancies"],
        data["glucose"],
        data["blood_pressure"],
        data["skin_thickness"],
        data["insulin"],
        data["bmi"],
        data["dpf"],
        data["age"]
    ]]

    # prediction
    prediction = model.predict(input_data)

    return jsonify({
        "prediction": str(prediction[0])
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))