# 💳 AI Fraud Detection System

An end-to-end machine learning project that detects fraudulent financial transactions using a LightGBM model and provides an interactive Streamlit dashboard for real-time predictions.

---

## 📌 Project Overview

Financial fraud is a major challenge in digital payment systems.  
This project builds a machine learning model capable of identifying suspicious transactions based on transaction patterns and account balance behavior.

The system includes:

• Exploratory Data Analysis  
• Feature Engineering  
• Machine Learning Model Training  
• Model Evaluation  
• Fraud Detection Dashboard (Streamlit)

---

## 🧠 Machine Learning Pipeline

The project follows a typical production ML workflow:

1. Data Cleaning
2. Exploratory Data Analysis
3. Feature Engineering
4. Logistic Regression Baseline Model
5. LightGBM Model Training
6. Cross-Validation
7. Threshold Optimization
8. Model Deployment with Streamlit

---

## 📊 Model Performance

| Metric | Score |
|------|------|
| ROC-AUC | 0.999 |
| PR-AUC | 0.95 |
| Precision | 0.95 |
| Recall | 0.78 |

The LightGBM model significantly improves fraud detection performance compared to the baseline logistic regression model.

---

## 📈 Key Fraud Indicators

Important features that helped detect fraudulent transactions:

• Transaction amount  
• Sender account balance before transaction  
• Balance difference after transaction  
• Destination account balance changes  
• Transaction type (TRANSFER / CASH_OUT)

These patterns match common fraud behaviors observed in financial systems.

---

## 🖥️ Fraud Detection Dashboard

An interactive dashboard built using Streamlit allows users to:

• Enter transaction details  
• Predict fraud probability  
• Visualize fraud risk  
• Upload CSV files for batch fraud detection  

---
