import streamlit as st
import pandas as pd
import numpy as np
from utils import get_sample_data, calculate_statistics

st.set_page_config(
    page_title="Streamlit Demo App",
    page_icon="??",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title("?? Streamlit Demo Application")
st.write("Bienvenido a esta aplicación de demostración de Streamlit")

st.sidebar.title("?? Opciones")
page = st.sidebar.radio(
    "Selecciona una página:",
    ["Inicio", "Datos y Gráficos", "Interactivos", "Acerca de"]
)

if page == "Inicio":
    st.header("Inicio")
    st.write("Esta es una aplicación de demostración de Streamlit")

elif page == "Datos y Gráficos":
    st.header("?? Datos y Gráficos")
    df = get_sample_data()
    st.dataframe(df)
    stats = calculate_statistics(df["valor"].tolist())
    st.metric("Promedio", f"{stats['media']:.2f}")

elif page == "Interactivos":
    st.header("??? Componentes Interactivos")
    valor = st.slider("Selecciona un valor:", 0, 100, 50)
    st.write(f"Valor: {valor}")

elif page == "Acerca de":
    st.header("?? Acerca de")
    st.write("App de Streamlit")
