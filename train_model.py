import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.neighbors import NearestNeighbors
import joblib

df = pd.read_csv("gift_dataset.csv")

df["combined_features"] = df.apply(lambda row: f"{row['Preferences']} {row['Hobbies']} {row['Job']} {row['Past Gifts']}", axis=1)

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(df["combined_features"])  

model = NearestNeighbors(n_neighbors=1, metric="cosine")  
model.fit(X)

joblib.dump(model, "GiftRecommendation.pkl")
joblib.dump(vectorizer, "vectorizer.pkl")
joblib.dump(df, "Gift_df.pkl") 

print("Model trained and saved successfully!")