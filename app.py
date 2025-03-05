from flask import Flask, render_template, request
import joblib
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

app = Flask(__name__)

model = joblib.load("GiftRecommendation.pkl")
vectorizer = joblib.load("vectorizer.pkl")
df = joblib.load("Gift_df.pkl")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    age = request.form.get("Age", "").strip()
    gender = request.form.get("Gender", "").strip()
    occasion = request.form.get("Occasion", "").strip()
    preferences = request.form.get("Preferences", "").strip()
    hobbies = request.form.get("Hobbies", "").strip()
    job = request.form.get("Job", "").strip()
    past_gifts = request.form.get("Past Gifts", "").strip()
    price_range = request.form.get("Price Range", "").strip()

    user_input = f"{age} {gender} {occasion} {preferences} {hobbies} {job} {past_gifts} {price_range}"

    if not user_input.strip():
        return "Error: No input provided. Please enter details.", 400

    input_vector = vectorizer.transform([user_input])
    _, indices = model.kneighbors(input_vector, n_neighbors=5)
    
    recommendations = df.iloc[indices[0]][["Preferences", "Hobbies", "Past Gifts", "Price Range"]]

    return render_template("result.html", user_input=user_input, recommendations=recommendations.to_dict(orient="records"))

if __name__ == "__main__":
    app.run(debug=True)

