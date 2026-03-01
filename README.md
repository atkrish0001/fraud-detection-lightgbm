# 💳 AI Fraud Detection System

An end-to-end machine learning project that detects fraudulent financial transactions using a LightGBM model and provides an interactive Streamlit dashboard for real-time fraud prediction.

---

# 📌 Project Overview

Financial fraud is a major issue in digital payment systems. Fraudulent transactions cause billions of dollars in losses globally each year.

This project builds a machine learning system capable of detecting suspicious financial transactions based on transaction patterns and account balance changes.

The system includes:

- Data exploration and visualization
- Feature engineering
- Machine learning model training
- Model evaluation
- Interactive fraud detection dashboard

---

# 🧠 Machine Learning Pipeline
Dataset
│
▼
Exploratory Data Analysis
│
▼
Feature Engineering
│
▼
Baseline Model (Logistic Regression)
│
▼
LightGBM Model Training
│
▼
Cross Validation
│
▼
Threshold Optimization
│
▼
Streamlit Fraud Detection Dashboard


---

# 📊 Model Performance

| Metric | Score |
|------|------|
| ROC-AUC | 0.999 |
| PR-AUC | 0.95 |
| Precision | 0.95 |
| Recall | 0.78 |

The LightGBM model significantly improves performance compared to the baseline logistic regression model.

---

# 📈 Key Fraud Indicators

Important features identified by the model:

- Transaction Amount
- Sender Balance Before Transaction
- Balance Difference After Transaction
- Receiver Balance Change
- Transaction Type (TRANSFER / CASH_OUT)

These features reflect common fraud patterns observed in financial systems.

---

# 🖥️ Fraud Detection Dashboard

The Streamlit dashboard allows users to:

- Enter transaction details
- Predict fraud probability
- Visualize fraud risk using a gauge chart
- Upload CSV files for batch fraud detection

---

# 📸 Dashboard Preview

![Dashboard](images/dashboard.png)

---

---

# 🚀 Future Improvements

- Real-time fraud monitoring
- Advanced feature engineering
- Hyperparameter tuning
- Cloud deployment
- Model explainability (SHAP)

---
