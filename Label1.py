import streamlit as st
import pytesseract
from PIL import Image, ImageOps
import numpy as np

st.title("📦 Lector de Labels con OCR")

uploaded_file = st.file_uploader("Sube una foto del label", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Mostrar imagen subida
    image = Image.open(uploaded_file)
    st.image(image, caption="Imagen subida", use_column_width=True)

    # Convertir a escala de grises (sin cv2)
    gray = ImageOps.grayscale(image)

    # OCR con pytesseract
    text = pytesseract.image_to_string(gray, lang="eng")

    st.subheader("Texto detectado:")
    st.text(text)

    # Procesamiento simple para buscar código, descripción y peso
    codigo, descripcion, peso = None, None, None

    for line in text.split("\n"):
        line = line.strip()
        if not line:
            continue
        if any(c.isdigit() for c in line) and codigo is None:
            codigo = line
        if "beer" in line.lower() or "original" in line.lower():
            descripcion = line
        if "ml" in line.lower() or "kg" in line.lower() or "g" in line.lower():
            peso = line

    st.subheader("📋 Datos extraídos")
    st.write(f"**Código:** {codigo if codigo else 'No encontrado'}")
    st.write(f"**Descripción:** {descripcion if descripcion else 'No encontrada'}")
    st.write(f"**Peso:** {peso if peso else 'No encontrado'}")
