# Heart Disease Prediction (UCI Dataset)

## Overview
This project is a beginner-to-intermediate machine learning walkthrough using the UCI Heart Disease dataset.  
The goal is to predict whether a patient has heart disease using clinical and demographic features.

This notebook focuses less on “just training a model” and more on **doing ML correctly**:
- Understanding the data
- Avoiding leakage
- Making conscious modeling decisions
- Interpreting results instead of blindly trusting accuracy

---

## Problem Definition
- **Domain:** Healthcare
- **Unit of observation:** One patient
- **Task:** Binary classification
- **Target:** Presence of heart disease
- **Risk level:** High (medical context)

The original dataset contains a multi-level target (`num` from 0–4).  
For learning purposes, this was converted into a **binary target**:

```txt
Positive = 1 if num > 0
Positive = 0 if num == 0
```

This simplifies the task while keeping clinical meaning.

---

## Dataset Summary
- **Rows:** 920 patients
- **Features:** 13 input features
- **Target:** Binary (Positive / Negative)

### Feature Groups
- **Demographics:** age, sex
- **Symptoms:** chest pain (cp), exercise-induced angina (exang)
- **Vitals & measurements:** trestbps, chol, thalch, oldpeak
- **Diagnostic tests:** restecg, slope, ca, thal

Identifier columns (`id`, `dataset`) were dropped to avoid leakage.

---

## Key Concepts Learned

### 1. Target Engineering
- Multi-class medical outcomes can often be reframed as binary for early modeling
- Always define the target **before** touching features

---

### 2. Categorical vs Numeric Features
Some columns look numeric but are actually categorical encodings.

Example:
```txt
0 = normal
1 = abnormal
2 = severe
```

These were treated as **categorical**, not continuous numbers.

This matters for:
- Scaling
- Encoding
- Model interpretability

---

### 3. Missing Data Awareness
No imputation was done initially.  
Instead, missingness was **observed and classified**:

- Low missingness → likely random
- Medium/high missingness → likely **systematic**
  - Advanced diagnostic tests not performed for all patients

This step prevents silent bias and unrealistic performance.

---

### 4. Leakage Check
Asked explicitly:
> “Does any feature describe something that happens after diagnosis?”

All retained features were measured **before** outcome determination.  
No leakage detected.

---

### 5. Proper Train/Test Split
- Used stratified splitting to preserve class balance
- Verified positive rates in train and test sets

```python
train_test_split(..., stratify=y)
```

This avoids misleading evaluation metrics.

---
### 6. Preprocessing the Right Way

Preprocessing was done inside a pipeline, not manually:
- Numeric features → StandardScaler
- Categorical features → OneHotEncoder
- Missing values → SimpleImputer

This prevents data leakage and keeps training/test logic consistent.

--- 
### 7. Model Training
Model used:
- Logistic Regression
- Scaled features
- Max iterations increased for convergence

Why Logistic Regression?
- Interpretable
- Strong Baseline
- Appropriate for binary medical risk prediction

---
### 8. Model Evaluation
Performance on the test set:
- Accuracy: ~83%
- Balanced precision and recall
- Confusion matrix inspected to understand error types
Accuracy alone was not trusted blindly

---
### 9. Feature Importance Interpretation
Logistic regression coefficients were extracted and mapped back to feature names.

Interpretation rules:
- Positive coefficient: increases risk
- Negative coefficient: decreases risk
- Magnitude = strength of influence (after scaling)

This provided real insight into which clinical factors matter most.

---
### 10. Single-Patient Prediction
Learned how to:
- Predict outcome for one patient
- Extract probability of the predicted class
- Avoid shape errors (iloc[[0]], not iloc[0])

This bridges model training → real-world usage.

---
## What This Project Is (and Isn't)
✅ A correct ML workflow
✅ A strong foundation for healthcare modeling
✅ Focused on reasoning, not magic accuracy

❌ Not a production model
❌ No hyperparameter tuning yet
❌ No clinical claims

---
## Next Steps
- Try a tree-based model (Random Forest, XGBoost)
- Compare calibration (probabilities vs outcomes)
- Handle missingness more strategically
- Evaluate fairness across demographic groups

---
## Takeaway
This project taught me that:

> Most ML mistakes happen before the model is trained.

Understanding the data, target, and assumptions mattered more than any algorithm choice.
