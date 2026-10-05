# app.py
import streamlit as st
import pandas as pd
import pickle
st.set_page_config(page_title="Salary Predictor")
st.title("Salary Predictor")
st.write("Enter years of experience to estimate salary.")
with open("model.pkl", "rb") as file:
    model = pickle.load(file)
experience = st.number_input(
    "Years of experience",
    min_value=0.6,
    max_value=14.8,
    value=5.0,
    step=0.1
)
input_data = pd.DataFrame({"Experience Years": [experience]})
prediction = model.predict(input_data)[0]
st.success(f"Predicted salary: {prediction:,.2f}")
st.write("Salary currency and time period are not specified in the dataset.")