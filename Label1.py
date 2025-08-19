import streamlit as st
from PIL import Image, ImageOps
import pytesseract

st.set_page_config(page_title="Lector de Etiquetas", layout="wide")
st.title("📋 Lector de etiquetas - Funciona en Streamlit Cloud")

uploaded_file = st.file_uploader("Sube una foto de la etiqueta", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Imagen subida", use_column_width=True)

    # Convertir a gris para OCR
    gray = ImageOps.grayscale(image)

    # Extraer texto con Tesseract
    try:
        text = pytesseract.image_to_string(gray, lang='eng')  # Cambiar 'spa' si deseas español
        st.subheader("Texto detectado:")
        st.text_area("Texto extraído", text, height=300)
    except pytesseract.TesseractNotFoundError:
        st.error("Tesseract no está disponible en el entorno. Streamlit Cloud maneja esto automáticamente.")
