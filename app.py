from flask import Flask, render_template, request
import numpy as np
import pickle

app = Flask(__name__)

# Load model & scaler
model = pickle.load(open("rf_model.pkl", "rb"))
scaler = pickle.load(open("scaler.pkl", "rb"))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        age = float(request.form["age"])
        sex = int(request.form["sex"])
        bmi = float(request.form["bmi"])
        children = int(request.form["children"])
        smoker = int(request.form["smoker"])
        region = int(request.form["region"])

        # scale numerical features
        scaled_data = scaler.transform([[age, bmi, children]])

        age = scaled_data[0][0]
        bmi = scaled_data[0][1]
        children = scaled_data[0][2]

        input_data = np.array([[age, sex, bmi, children, smoker, region]])

        prediction = model.predict(input_data)[0]

        return render_template("index.html", prediction_text=f"Estimated Insurance Cost: ₹ {round(prediction,2)}")

    except:
        return render_template("index.html", prediction_text="Error in input")

if __name__ == "__main__":
    app.run(debug=True)