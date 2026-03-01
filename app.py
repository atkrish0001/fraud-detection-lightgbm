import streamlit as st
import pandas as pd
import joblib
import plotly.graph_objects as go

# Load model
model = joblib.load("fraud_lightgbm_model.pkl")

st.set_page_config(page_title="Fraud Detection Dashboard", layout="wide")

st.title("💳 AI Fraud Detection Dashboard")

st.markdown(
"""
This tool predicts whether a **financial transaction is fraudulent**.

Enter the transaction details below.

Example scenario:
- Customer transfers money to another account
- Balance changes after the transaction
- System evaluates if the behavior matches fraud patterns
"""
)

# Sidebar explanation
st.sidebar.header("Field Explanation")

st.sidebar.markdown("""
**Transaction Type**
- PAYMENT – bill payment
- TRANSFER – money sent to another account
- CASH_OUT – withdrawal to cash
- CASH_IN – deposit
- DEBIT – card debit

**Amount**
Total transaction amount.

**Old Balance Origin**
Balance of sender before transaction.

**New Balance Origin**
Balance of sender after transaction.

**Old Balance Destination**
Balance of receiver before transaction.

**New Balance Destination**
Balance of receiver after transaction.
""")

# User inputs
col1, col2 = st.columns(2)

with col1:

    type_transaction = st.selectbox(
        "Transaction Type",
        ["PAYMENT", "TRANSFER", "CASH_OUT", "DEBIT", "CASH_IN"]
    )

    amount = st.number_input(
        "Transaction Amount",
        value=5000,
        help="Example: 5000 means ₹5000 transaction"
    )

    oldbalanceOrg = st.number_input(
        "Sender Balance Before Transaction",
        value=10000,
        help="Example: Account had ₹10000 before sending money"
    )

with col2:

    newbalanceOrig = st.number_input(
        "Sender Balance After Transaction",
        value=5000,
        help="Example: Balance becomes ₹5000 after sending ₹5000"
    )

    oldbalanceDest = st.number_input(
        "Receiver Balance Before Transaction",
        value=2000,
        help="Example: Receiver account previously had ₹2000"
    )

    newbalanceDest = st.number_input(
        "Receiver Balance After Transaction",
        value=7000,
        help="Example: Receiver gets ₹5000 so new balance ₹7000"
    )

# Feature engineering
balanceDiffOrig = oldbalanceOrg - newbalanceOrig
balanceDiffDest = newbalanceDest - oldbalanceDest

# Prediction
if st.button("Predict Fraud"):

    input_data = pd.DataFrame({
        "type":[type_transaction],
        "amount":[amount],
        "oldbalanceOrg":[oldbalanceOrg],
        "newbalanceOrig":[newbalanceOrig],
        "oldbalanceDest":[oldbalanceDest],
        "newbalanceDest":[newbalanceDest],
        "balanceDiffOrig":[balanceDiffOrig],
        "balanceDiffDest":[balanceDiffDest]
    })

    prob = model.predict_proba(input_data)[:,1][0]

    st.subheader("Fraud Risk Score")

    # Gauge chart
    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=prob*100,
        title={'text': "Fraud Probability (%)"},
        gauge={
            'axis': {'range': [0,100]},
            'bar': {'color': "red"},
            'steps': [
                {'range': [0,40], 'color': "green"},
                {'range': [40,70], 'color': "yellow"},
                {'range': [70,100], 'color': "red"}
            ]
        }
    ))

    st.plotly_chart(fig)

    if prob > 0.995:
        st.error("High Fraud Risk")
    elif prob > 0.7:
        st.warning("Suspicious Transaction")
    else:
        st.success("Transaction Appears Legitimate")

# CSV Upload Section
st.markdown("---")
st.header("Batch Fraud Detection")

uploaded_file = st.file_uploader("Upload CSV file with transactions")

if uploaded_file:

    data = pd.read_csv(uploaded_file)

    st.write("Preview of uploaded data:")
    st.dataframe(data.head())

    preds = model.predict_proba(data)[:,1]

    data["Fraud_Probability"] = preds
    data["Fraud_Prediction"] = (preds > 0.995).astype(int)

    st.write("Prediction Results")
    st.dataframe(data.head())

    st.download_button(
        label="Download Results CSV",
        data=data.to_csv(index=False),
        file_name="fraud_predictions.csv"
    )