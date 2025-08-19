import streamlit as st
from PIL import Image, ImageOps
import pytesseract
import os

st.title("📋 Lector de etiquetas - Streamlit Cloud")

# Configurar ruta de Tesseract para Streamlit Cloud
if os.name != "nt":  # Linux/Mac (Streamlit Cloud usa Linux)
    pytesseract.pytesseract.tesseract_cmd = "/usr/bin/tesseract"

uploaded_file = st.file_uploader("Sube una foto de la etiqueta", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Imagen subida", use_column_width=True)

    gray = ImageOps.grayscale(image)

    try:
        text = pytesseract.image_to_string(gray, lang="eng")  # o 'spa'
        st.subheader("Texto detectado:")
        st.text_area("Texto extraído", text, height=300)
    except pytesseract.TesseractNotFoundError:
        st.error("Tesseract no se encuentra en el entorno.")
