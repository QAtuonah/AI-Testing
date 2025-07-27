# ⚖️ Test Model Fairness
# Checa se o modelo tem viés para determinada categoria (ex: gênero, região).

import pandas as pd
import joblib
from collections import Counter

model = joblib.load("trained_model.pkl")
df = pd.read_csv("../datasets/input_data_sample.csv")

# Supondo que haja uma coluna sensível, por exemplo: 'country'
def test_fairness(df):
    sensitive_column = "country"
    if sensitive_column not in df.columns:
        print("⚠️ No sensitive column found for fairness test.")
        return

    for group in df[sensitive_column].unique():
        subset = df[df[sensitive_column] == group].drop(columns=["userId"])
        preds = model.predict(subset)
        print(f"{group}: {Counter(preds)}")

if __name__ == "__main__":
    test_fairness(df)
