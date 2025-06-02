import streamlit as st
import numpy as np
import joblib

st.title("AI-Driven Waste-to-Energy (WTE) Simulator")

@st.cache_resource
def load_model():
    return joblib.load("ai_model.pkl")

model = load_model()

st.header("Input Waste Parameters")
organic = st.slider("Organic content (%)", 10, 80, 40)
moisture = st.slider("Moisture content (%)", 5, 50, 25)
plastic = st.slider("Plastic content (%)", 0, 50, 15)
temperature = st.slider("Gasifier temperature (°C)", 600, 1000, 850)
equiv_ratio = st.slider("Equivalence Ratio (O₂/Fuel)", 0.2, 0.5, 0.35)

X_input = np.array([[organic, moisture, plastic, temperature, equiv_ratio]])
predicted_energy = model.predict(X_input)[0]

st.subheader("Predicted Output")
st.write(f"🔋 **Syngas Energy Yield:** {predicted_energy:.2f} kWh/ton")
