import streamlit as st
from PIL import Image
import pytesseract
import cv2
import numpy as np

# Si Tesseract no está en el PATH, descomenta y coloca tu ruta
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

st.title("📋 Lector de etiquetas")

# Subir imagen
uploaded_file = st.file_uploader("Sube una foto de la etiqueta", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Imagen subida", use_column_width=True)

    image_cv = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
    gray = cv2.cvtColor(image_cv, cv2.COLOR_BGR2GRAY)
    text = pytesseract.image_to_string(gray, lang='eng')
    
    st.subheader("Texto detectado:")
    st.text_area("Texto extraído", text, height=300)
