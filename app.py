from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# Load trained SVM model
model = pickle.load(open("model.pkl", "rb"))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        work_hours = float(request.form["work_hours"])
        remote_work = 1 if request.form["remote_work"].lower() == "yes" else 0
        company_support = 1 if request.form["company_support"].lower() == "yes" else 0

        stress_level_map = {"Low": 1, "Medium": 2, "High": 0}
        stress_level = stress_level_map[request.form["stress_level"]]

        past_history = 1 if request.form["past_history"].lower() == "yes" else 0

        # Prepare input
        features = np.array([[work_hours, remote_work, company_support, stress_level, past_history]])

        prediction = model.predict(features)[0]
        result = "Yes - Likely to face mental health issues" if prediction == 1 else "No - Unlikely to face mental health issues"

        return render_template("result.html", result=result)

    except Exception as e:
        return f"Error: {e}"

if __name__ == "__main__":
    app.run(debug=True)
