import streamlit as st
from PIL import Image, ImageOps
import pytesseract

# ---------------------------
# Configurar ruta de Tesseract si no está en PATH
# Windows ejemplo:
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
# Linux/Mac ejemplo (normalmente no es necesario)
# pytesseract.pytesseract.tesseract_cmd = r'/usr/bin/tesseract'
# ---------------------------

st.title("📋 Lector de etiquetas")

# Subir imagen
uploaded_file = st.file_uploader("Sube una foto de la etiqueta", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Imagen subida", use_column_width=True)

    # Convertir a escala de grises para mejorar OCR
    gray = ImageOps.grayscale(image)

    # Extraer texto
    try:
        text = pytesseract.image_to_string(gray, lang='eng')  # o 'spa' para español
        st.subheader("Texto detectado:")
        st.text_area("Texto extraído", text, height=300)
    except pytesseract.TesseractNotFoundError:
        st.error("Tesseract OCR no está instalado o no se encuentra en el PATH. Revisa la configuración.")
