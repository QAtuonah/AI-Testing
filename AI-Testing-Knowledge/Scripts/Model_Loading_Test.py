# ✅ Model Loading Test
# Verifica se o modelo pode ser carregado corretamente sem erros.

import joblib
import os

MODEL_PATH = "trained_model.pkl"

def test_model_loading():
    assert os.path.exists(MODEL_PATH), f"Model not found at {MODEL_PATH}"
    try:
        model = joblib.load(MODEL_PATH)
        print("✅ Model loaded successfully.")
    except Exception as e:
        raise AssertionError(f"❌ Failed to load model: {e}")

if __name__ == "__main__":
    test_model_loading()
