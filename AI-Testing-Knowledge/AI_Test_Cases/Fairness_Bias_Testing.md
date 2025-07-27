# ⚖️ Fairness & Bias Testing

Testing whether the model produces equitable results across different user groups.

## 💡 Test Case 1: Demographic Parity
- **Objective:** Validate that prediction rates are equal across groups (e.g., gender).
- **Steps:**
  1. Run predictions for group A and B.
  2. Compare positive prediction rates.
- **Expected Result:** Rate difference should not exceed defined threshold (e.g., 10%).

---

## 💡 Test Case 2: Equal Opportunity
- **Objective:** Check that model has equal true positive rates across groups.
- **Steps:**
  1. Compare TPR (true positives / positives) per group.
- **Expected Result:** Equal TPR within acceptable margin.

---

## 💡 Test Case 3: Analyze Bias in Features
- **Objective:** Ensure no protected features (e.g., gender, race) are over-weighted.
- **Steps:**
  1. Analyze model weights or SHAP values.
- **Expected Result:** Protected attributes have low or no influence unless justified.

---

## 💡 Test Case 4: Outlier Impact Across Groups
- **Objective:** Check if one group suffers more from misclassification in outlier scenarios.
- **Steps:**
  1. Test outliers in each group.
- **Expected Result:** Performance remains balanced.
