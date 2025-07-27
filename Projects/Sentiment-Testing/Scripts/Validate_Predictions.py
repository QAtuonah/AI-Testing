import pandas as pd
import joblib
from sklearn.metrics import classification_report

model = joblib.load("sentiment_model.pkl")
data = pd.read_csv("datasets/sample_reviews.csv")

X = data["review_text"]
y_true = data["label"]

y_pred = model.predict(X)
print(classification_report(y_true, y_pred))
