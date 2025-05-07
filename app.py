import streamlit as st
from streamlit_drawable_canvas import st_canvas

# Estilos personalizados
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Raleway:wght@600&display=swap');

    html, body, [class*="css"]  {
        font-family: 'Raleway', sans-serif;
    }

    .sidebar .stSelectbox label,
    .sidebar .stSlider label,
    .sidebar .stColorPicker label {
        font-size: 16px;
        color: #000000;  /* Letra en negro */
    }

    .sidebar {
        background-color: #FAEBD7;
        border-radius:


