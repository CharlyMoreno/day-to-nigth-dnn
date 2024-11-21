import os
import streamlit as st
from PIL import Image, ImageOps

st.set_page_config(page_title="Transformación de Imágenes", layout="wide")


with st.container():
    col1, col2 = st.columns([3, 1])
    with col1:
        st.title("Dia a Noche - Converti tu imagen")
        st.subheader("Redes Neuronales Profundas")
    with col2:
        logo = "utn.png"
        st.image(logo, use_container_width=True)



uploaded_file = st.file_uploader("Sube una imagen", type=["jpg", "jpeg", "png"])

st.markdown("<br>", unsafe_allow_html=True)

col_button = st.columns([3, 1, 3])[1]

with col_button:
    transform = st.button("Convertir imagen a noche")

if uploaded_file:
    original_image = Image.open(uploaded_file)
    transformed_image = None

    if transform:
        transformed_image = ImageOps.grayscale(original_image)

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Imagen Original")
        st.image(original_image, caption="Original", use_container_width=True)

    with col2:
        st.subheader("Imagen Transformada")
        if transformed_image:
            st.image(transformed_image, caption="Transformada", use_container_width=True)
        else:
            st.info("Presiona 'Convertir imagen a noche' para ver el resultado.")

st.markdown(
    """
    <hr style='margin-top: 50px;'>
    <div style='text-align: center; font-size: 14px;'>
        Redes Neuronales Profundas 2024 - UTN FRM 2024
    </div>
    """,
    unsafe_allow_html=True,
)