from PIL import Image, ImageOps
import pytesseract
import streamlit as st

st.title("📋 Lector de etiquetas (sin OpenCV)")

uploaded_file = st.file_uploader("Sube una foto", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Imagen subida", use_column_width=True)

    gray = ImageOps.grayscale(image)  # convierte a gris
    text = pytesseract.image_to_string(gray, lang='eng')

    st.subheader("Texto detectado:")
    st.text_area("Texto extraído", text, height=300)
