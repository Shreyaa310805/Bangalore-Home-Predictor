import streamlit as st
import pandas as pd

st.set_page_config(page_title="Bangalore Property Pulse", layout="wide")

st.title("₹ Bangalore House Price Intelligence")
st.markdown("### 3rd Year Engineering Project | Machine Learning Analysis")

# Sidebar Inputs
st.sidebar.header("Property Details")
loc = st.sidebar.selectbox("Location", ["Whitefield", "Electronic City", "Sarjapur Road", "HSR Layout", "Indiranagar", "Hebbal"])
sqft = st.sidebar.slider("Total Sq. Ft.", 500, 5000, 1200)
bhk = st.sidebar.selectbox("BHK", [1, 2, 3, 4, 5])

# Simple logic for the demo (Mocking the ML model weights for Bangalore)
base_prices = {"Whitefield": 7500, "Electronic City": 5500, "Sarjapur Road": 6500, "HSR Layout": 9500, "Indiranagar": 15000, "Hebbal": 8500}
price_per_sqft = base_prices[loc]
prediction = (price_per_sqft * sqft) + (bhk * 200000)

# Display Results
col1, col2 = st.columns(2)
with col1:
    st.metric("Estimated Price", f"₹ {prediction/100000:.2f} Lakhs")
with col2:
    st.metric("Price per Sq. Ft.", f"₹ {price_per_sqft}")

st.bar_chart(pd.DataFrame(base_prices.items(), columns=['Location', 'Price']).set_index('Location'))
