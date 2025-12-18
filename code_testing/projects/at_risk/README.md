# Student Academic Risk Prediction (Practice Project)

This project is a **practice machine learning project** built to understand the full end-to-end ML workflow in preparation for Hacklytics.  
The goal was not to build a production system, but to **learn how ML models are framed, trained, evaluated, and interpreted** in a realistic setting.

---

## Project Goal

The objective of this project is to predict whether a student is **academically at risk** based on demographic, behavioral, and support-related features.

We frame this as a **binary classification problem**:

- `AtRisk = 1` if GPA < 2.5  
- `AtRisk = 0` otherwise

The emphasis is on **early risk detection**, not perfect accuracy.

---

## Dataset

- Public student performance dataset
- 2,392 students
- 12 input features after preprocessing

### Example Features
- StudyTimeWeekly
- Absences
- Tutoring
- ParentalSupport
- Extracurricular activities
- Sports / Music / Volunteering
- Age, Gender, Ethnicity

Performance-related fields such as GPA were **excluded from training** to prevent label leakage.

---

## Methodology

### 1. Problem Framing
- Converted GPA into a binary risk label
- Ensured the model predicts risk *without directly seeing GPA*

### 2. Train/Test Split
- 80/20 split
- Stratified by risk label to preserve class distribution
- Ensured fair and representative evaluation

### 3. Model Choice
- **Logistic Regression**
- Chosen for:
  - Interpretability
  - Simplicity
  - Ability to explain feature influence

### 4. Pipeline
A Scikit-Learn pipeline was used to ensure consistent preprocessing:

- StandardScaler for feature scaling
- LogisticRegression classifier

This prevents data leakage and ensures reproducibility.

---

## Evaluation Metrics

Given class imbalance, evaluation focused on **recall for AtRisk students** rather than accuracy alone.

### Results (Test Set)

- Accuracy: **~93%**
- Recall (AtRisk): **~96%**
- Precision (AtRisk): **~94%**

Confusion matrix analysis showed the model successfully identified most at-risk students while keeping false alarms reasonable.

---

## Model Interpretation

Because logistic regression was used, feature coefficients were directly interpretable.

### Key Insights
- **Strong protective factors**:
  - ParentalSupport
  - StudyTimeWeekly
  - Tutoring
  - Extracurricular involvement

- **Negligible influence**:
  - ParentalEducation had a near-zero coefficient, suggesting minimal predictive value once behavioral factors were included.

This reinforced the idea that **direct support and habits matter more than background credentials** in predicting risk.

---

## Individual Prediction Demo

The model can generate predictions for individual students, including:
- Risk classification (AtRisk / NotAtRisk)
- Confidence score using predicted class probability

This demonstrates how the model could support targeted academic interventions.

---

## What I Learned

Through this project, I learned how to:

- Frame real-world problems as supervised ML tasks
- Engineer labels responsibly
- Prevent data leakage
- Use pipelines for clean preprocessing
- Evaluate models beyond accuracy
- Interpret coefficients instead of treating models as black boxes
- Communicate ML results clearly and defensibly

Most importantly, I learned that **ML is more about structure, decisions, and interpretation than complex algorithms**.

---

## Next Steps (Practice Roadmap)

This project is part of a broader practice plan leading up to Hacklytics. Future improvements include:

- Threshold tuning for recall-precision tradeoffs
- Feature encoding improvements for categorical variables
- Comparing multiple baseline models
- Improving storytelling and demo presentation

---

## Disclaimer

This project is for **learning and practice purposes only** and does not claim causal conclusions.  
All findings are correlational and dataset-dependent.
