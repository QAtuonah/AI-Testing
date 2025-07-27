# 🔍 Test Data Integrity
# Verifica se os dados de entrada possuem colunas esperadas e estão sem valores ausentes.

import pandas as pd

REQUIRED_COLUMNS = ["userId", "productId", "price", "stock", "categoryId"]
DATA_PATH = "../datasets/input_data_sample.csv"

def test_data():
    df = pd.read_csv(DATA_PATH)
    missing_columns = [col for col in REQUIRED_COLUMNS if col not in df.columns]
    assert not missing_columns, f"Missing columns: {missing_columns}"
    assert df.isnull().sum().sum() == 0, "❌ Dataset contains null values"
    print("✅ Data integrity test passed.")

if __name__ == "__main__":
    test_data()
