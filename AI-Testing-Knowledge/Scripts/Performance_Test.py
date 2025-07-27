# ⏱️ Model Performance Test
# Mede o tempo que o modelo leva para processar uma quantidade de previsões.

import time
import joblib
import pandas as pd

model = joblib.load("trained_model.pkl")
df = pd.read_csv("../datasets/input_data_sample.csv")

def test_performance():
    start = time.time()
    _ = model.predict(df)
    duration = time.time() - start
    print(f"✅ Model prediction time: {duration:.3f}s for {len(df)} rows.")

if __name__ == "__main__":
    test_performance()
