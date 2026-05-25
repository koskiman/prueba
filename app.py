import streamlit as st
import pandas as pd
import numpy as np
from utils import get_sample_data, calculate_statistics

st.set_page_config(
    page_title="Streamlit Demo App",
    page_icon="chart",
    layout="wide"
)

st.title("Streamlit Demo Application")
st.write("Welcome to this Streamlit demonstration application")

st.sidebar.title("Options")
page = st.sidebar.radio(
    "Select a page:",
    ["Home", "Data and Charts", "Interactive", "About"]
)

if page == "Home":
    st.header("Home")
    st.write("This is a Streamlit demonstration application")

elif page == "Data and Charts":
    st.header("Data and Charts")
    df = get_sample_data()
    st.dataframe(df)
    stats = calculate_statistics(df["valor"].tolist())
    st.metric("Average", f"{stats['media']:.2f}")
    st.line_chart(df.set_index("mes")["valor"])

elif page == "Interactive":
    st.header("Interactive Components")
    valor = st.slider("Select a value:", 0, 100, 50)
    st.write(f"Selected value: {valor}")
    
    nombre = st.text_input("Enter your name:")
    if nombre:
        st.write(f"Hello, {nombre}!")
    
    if st.button("Click me"):
        st.success("Button pressed!")

elif page == "About":
    st.header("About")
    st.write("Streamlit Demo App - Simple application demonstration")
