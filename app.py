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

    .main-title {
        font-size: 48px;
        color: #FF5733;
        text-align: center;
        margin-bottom: -20px;
        animation: fadeIn 2s ease-in-out;
    }

    .sidebar .stSelectbox label,
    .sidebar .stSlider label,
    .sidebar .stColorPicker label {
        font-size: 16px;
        color: #000000;
    }

    .sidebar {
        background-color: #eebb78;
        border-radius: 12px;
        padding: 20px 10px;
    }

    .stSlider, .stSelectbox, .stColorPicker {
        background-color: #FFF0F5;
        border-radius: 10px;
        padding: 6px 12px;
    }

    @keyframes fadeIn {
        from {opacity: 0;}
        to {opacity: 1;}
    }

    
    </style>

    <div class="main-title"> Tablero Creativo </div>
    """,
    unsafe_allow_html=True
)

# Configuración del tablero en la barra lateral
with st.sidebar:
    st.markdown("### Personaliza tu experiencia")
    drawing_mode = st.selectbox(
        "Herramienta de dibujo:",
        ("freedraw", "line", "rect", "circle", "transform", "polygon", "point")
    )
    stroke_width = st.slider("Ancho del trazo", 1, 30, 10)
    stroke_color = st.color_picker("Color del trazo", "#FF5733")
    bg_color = "#eebb78"  # fondo pastel cálido

# Lienzo con espacio extra y configuración ideal
st.markdown('<div class="canvas-container">', unsafe_allow_html=True)

canvas_result = st_canvas(
    fill_color="#FFFFFFF",  # fondo blanco cálido
    stroke_width=stroke_width,
    stroke_color=stroke_color,
    background_color=bg_color,
    height=700,
    width=1000,
    drawing_mode=drawing_mode,
    key="canvas"
)

st.markdown('</div>', unsafe_allow_html=True)

