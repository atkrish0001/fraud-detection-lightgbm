# AI Fraud Detection System

This project detects fraudulent financial transactions using LightGBM and provides an interactive Streamlit dashboard for real-time predictions.

## Features

- Fraud detection using LightGBM
- Interactive Streamlit dashboard
- Fraud probability visualization
- Batch fraud detection via CSV upload
- Model evaluation using ROC-AUC and PR-AUC

## Model Performance

ROC-AUC: 0.999  
PR-AUC: 0.95  
Precision: 0.95  
Recall: 0.78  

## Run the Project

pip install -r requirements.txt

python -m streamlit run app/app.py
