import streamlit as st
import random

st.title("Lanzar una moneda")

if st.button("Lanzar la moneda"):
    resultado = random.choice(["Cara", "Cruz"])
    st.write(f"¡La moneda cayó en: **{resultado}**!")