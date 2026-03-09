import streamlit as st
import numpy as np
import joblib

model = joblib.load("bankruptcy_model.pkl")

st.title("Bankruptcy Prediction")

debt_networth = st.number_input("Total debt / Total net worth")
ni_assets = st.number_input("Net Income to Total Assets")
interest_rate = st.number_input("Continuous interest rate (after tax)")
retained_assets = st.number_input("Retained Earnings to Total Assets")
borrowing_dep = st.number_input("Borrowing dependency")
after_tax_interest = st.number_input("After-tax net Interest Rate")
eps_persistence = st.number_input("Persistent EPS in last 4 seasons")
ni_equity = st.number_input("Net Income to Stockholder's Equity")
liability_equity = st.number_input("Liability to Equity")
profit_per_share = st.number_input("Per Share Net profit before tax")

if st.button("Predict"):
    features = np.array([[debt_networth,
                          ni_assets,
                          interest_rate,
                          retained_assets,
                          borrowing_dep,
                          after_tax_interest,
                          eps_persistence,
                          ni_equity,
                          liability_equity,
                          profit_per_share]])

    prediction = model.predict(features)

    if prediction == 1:
        st.error("High Bankruptcy Risk")
    else:
        st.success("Financially Stable")
