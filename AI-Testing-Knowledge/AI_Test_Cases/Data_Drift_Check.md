# 🔄 Data Drift Detection Test Cases

Test cases to detect if the input data distribution has significantly changed from the original training data.

## 📊 Test Case 1: Schema Mismatch Check
- **Objective:** Detect if the incoming data schema differs from training schema.
- **Steps:**
  1. Compare new data schema to baseline.
- **Expected Result:** Raise warning on mismatch (column missing, new column, type change).

---

## 📊 Test Case 2: Statistical Drift Detection (Kolmogorov–Smirnov)
- **Objective:** Identify significant distribution drift using statistical tests.
- **Steps:**
  1. Compare historical vs current data for selected features.
- **Expected Result:** Drift flagged if p-value < 0.05.

---

## 📊 Test Case 3: Feature Importance Change
- **Objective:** Check if model relies on different features due to drift.
- **Steps:**
  1. Recalculate feature importance on new data.
- **Expected Result:** Significant shift (>20%) in importance should trigger alert.

---

## 📊 Test Case 4: Prediction Output Drift
- **Objective:** Monitor change in predicted class/probability distributions.
- **Steps:**
  1. Track class prediction frequency or probability histograms over time.
- **Expected Result:** Major change triggers alert (e.g., class X now occurs 3x more).
