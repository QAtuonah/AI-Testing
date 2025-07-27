# ⚠️ AI Risk Assessment Notes

## 🔍 Model Risks Identified

- **Bias by Geography:** Slight overprediction for users from Brazil.
- **Missing Values:** Certain records missing `categoryId` — handled via fallback, but needs review.
- **Overfitting Signs:** Accuracy drops significantly with unseen product types.

---

## 🔐 Security & Privacy Concerns

- Model input includes `email` and `address1` fields — ensure anonymization before logging.
- Check for potential leakage of PII during logging or debugging.

---

## 🔄 Next Actions

- Retrain model excluding unnecessary personal identifiers.
- Introduce additional test cases for outlier inputs.
- Improve test coverage on explainability outputs.
