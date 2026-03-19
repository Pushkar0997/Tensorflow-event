import streamlit as st
import numpy as np
from pathlib import Path
from tensorflow import keras

# Absolute path relative to this app.py file
MODEL_PATH = Path(__file__).resolve().parent / "Model" / "diabetes_model.keras"

@st.cache_resource
def load_model():
    if not MODEL_PATH.exists():
        raise FileNotFoundError(f"Model not found at: {MODEL_PATH}")
    return keras.models.load_model(MODEL_PATH)

model = load_model()

st.title("Diabetes Risk Prediction (Neural Network)")
st.write(
    "This app uses a TensorFlow neural network trained on the "
    "Pima Indians Diabetes dataset."
)

st.sidebar.header("Input features")

pregnancies = st.sidebar.number_input("Pregnancies", min_value=0, max_value=20, value=1)
glucose = st.sidebar.slider("Glucose", min_value=0, max_value=200, value=120)
blood_pressure = st.sidebar.slider("Blood Pressure", min_value=0, max_value=150, value=70)
skin_thickness = st.sidebar.slider("Skin Thickness", min_value=0, max_value=100, value=20)
insulin = st.sidebar.slider("Insulin", min_value=0, max_value=900, value=80)
bmi = st.sidebar.slider("BMI", min_value=0.0, max_value=70.0, value=25.0)
diabetes_pedigree = st.sidebar.slider("Diabetes Pedigree Function", min_value=0.0, max_value=3.0, value=0.5)
age = st.sidebar.slider("Age", min_value=18, max_value=100, value=30)

input_data = np.array(
    [[pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, diabetes_pedigree, age]],
    dtype="float32",
)

if st.button("Predict"):
    prob = float(model.predict(input_data, verbose=0)[0, 0])
    st.write(f"**Estimated probability of diabetes: {prob:.2f}**")

    if prob >= 0.5:
        st.error("Model prediction: High risk (class 1)")
    else:
        st.success("Model prediction: Low risk (class 0)")