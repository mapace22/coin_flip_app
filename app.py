import streamlit as st

st.header('Prueba')
number_of_trials = st.slider('¿Número de intentos?', 1, 1000, 10)
start_button = st.button('Ejecutar')

if start_button:
    st.write(f'Seleccionaste {number_of_trials} intentos.')