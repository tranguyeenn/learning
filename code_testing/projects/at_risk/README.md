# ML Practice Run #1 — What I Learned

This repository documents my **first complete end-to-end machine learning practice run**.  
The goal was not to build something impressive, but to **understand every step well enough to explain it without guessing**.

This project is part of my preparation for Hacklytics. I plan to repeat this process on multiple datasets and progressively add new techniques.

---

## Why I Did This

Before this project, I had:
- Heard ML terms
- Seen code snippets
- Zero confidence that I actually *understood* what was happening

This run was meant to answer:
- What does an ML pipeline actually look like?
- What decisions matter vs what is just boilerplate?
- How do I know if a model is actually good?

---

## What I Built (High Level)

- Binary classification model to predict **academic risk**
- Logistic regression with feature scaling
- Evaluated on a held-out test set
- Interpreted model coefficients
- Generated individual predictions with confidence scores

More important than *what* I built is **what I learned while building it**.

---

## Key Things I Learned

### 1. ML Is About Framing, Not Algorithms
The hardest and most important part was:
- Defining the label (`AtRisk`)
- Choosing a reasonable threshold
- Preventing data leakage

Once the problem was framed correctly, the model choice was almost secondary.

---

### 2. Train/Test Split Is About Fairness, Not Accuracy
I learned that:
- Matching train/test class distributions does NOT make the model more accurate
- It makes the **evaluation trustworthy**
- Stratification ensures the test set represents reality

This clarified the difference between:
- Experimental validity
- Model performance

---

### 3. Accuracy Can Be Misleading
Because the dataset was imbalanced:
- A naive model could achieve high accuracy
- Precision and recall were more meaningful

This forced me to:
- Look at the confusion matrix
- Focus on recall for at-risk students
- Think about the cost of false negatives

---

### 4. Pipelines Prevent Silent Mistakes
Using a `Pipeline` taught me:
- Why scaling must be fit only on training data
- How pipelines prevent data leakage
- How preprocessing and modeling should be treated as one unit

This made the workflow feel much more disciplined and reproducible.

---

### 5. Coefficients Matter More Than “AI Magic”
Interpreting logistic regression coefficients was one of the biggest insights.

I learned:
- The **sign** tells direction (risk-increasing vs protective)
- The **magnitude** tells importance
- Values near zero contribute almost nothing

Seeing features like:
- Study time
- Parental support
- Tutoring

dominate the model made the results feel intuitive and defensible.

---

### 6. Probability ≠ Prediction
Understanding `predict_proba` vs `predict` cleared up a lot of confusion.

Key realization:
- `predict()` gives a decision
- `predict_proba()` gives uncertainty
- Indexing probabilities is just array logic, not ML magic

This helped demystify confidence scores and thresholds.

---

### 7. ML Is Iterative by Design
This project made it clear that:
- One model run is not “the answer”
- Thresholds, features, and assumptions can all be tuned
- Improvement comes from iteration, not complexity

This changed how I think about “finishing” an ML project.

---

## What Still Feels Weak (On Purpose)

Things I *haven’t* mastered yet:
- Proper categorical encoding (one-hot vs ordinal)
- Threshold optimization strategies
- Model comparison beyond logistic regression
- Fairness and bias evaluation

These are intentional gaps for future practice runs.

---

## How This Informs My Next Practice Run

For the next dataset, I plan to:
- Rebuild the same pipeline from memory
- Tune classification thresholds
- Explicitly analyze precision–recall tradeoffs
- Improve how I communicate results

The goal is not novelty, but **depth and repetition**.

---

## Meta Reflection

This run taught me that:
> Machine learning is less about advanced math and more about careful decisions, clean structure, and honest evaluation.

I now feel confident explaining:
- What my model does
- Why I chose it
- What its limitations are

That confidence is the real output of this project.