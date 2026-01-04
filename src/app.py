from utils import db_connect
engine = db_connect()

import streamlit as st
import joblib

@st.cache_resource  # Esto optimiza la carga en 2026
def load_model():
    return joblib.load("modelo_entrenado.pkl")

model = load_model()

