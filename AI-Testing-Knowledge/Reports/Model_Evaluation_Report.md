# 📊 Model Evaluation Report

**Model:** Customer Purchase Prediction  
**Version:** v1.0  
**Test Date:** 2025-07-25  
**Tested by:** Christopher Atuonah

---

## ✅ Summary

- Accuracy: 92%
- Precision: 89%
- Recall: 94%
- F1-Score: 91.4%

---

## 📉 Confusion Matrix

|           | Predicted: Yes | Predicted: No |
|-----------|----------------|---------------|
| Actual: Yes | 47             | 3             |
| Actual: No  | 5              | 45            |

---

## 📌 Observations

- Model shows a slight tendency to overpredict positives.
- Performance is consistent across the majority of tested countries.
- Edge case for products with `stock = 0` returned unexpected results in 2 cases.

---

## 🧪 Recommendations

- Add specific checks for low-stock or out-of-stock items.
- Retrain with recent sales data for Brazil and India to improve accuracy in those regions.
