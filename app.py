import streamlit as st
import pandas as pd
import joblib

# Load trained model
model = joblib.load('logistic_regression_model.pkl')

st.title("⚙️ Machine Failure Prediction")
st.write("Predict if a machine will fail based on its operating parameters.")

# Input fields
air_temp = st.number_input("Air Temperature [K]", 295.0)
process_temp = st.number_input("Process Temperature [K]", 305.0)
rotational_speed = st.number_input("Rotational Speed [rpm]", 1400)
torque = st.number_input("Torque [Nm]", 45.0)
tool_wear = st.number_input("Tool Wear [min]", 100)

# Predict button
if st.button("Predict Failure"):
    data = [[air_temp, process_temp, rotational_speed, torque, tool_wear]]
    prediction = model.predict(data)[0]
    if prediction == 1:
        st.error("⚠️ Machine is likely to fail!")
    else:
        st.success("✅ Machine is functioning normally.")
