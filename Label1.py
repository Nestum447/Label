import streamlit as st
from transformers import TrOCRProcessor, VisionEncoderDecoderModel
from PIL import Image

st.title("OCR con HuggingFace")

processor = TrOCRProcessor.from_pretrained("microsoft/trocr-base-stage1")
model = VisionEncoderDecoderModel.from_pretrained("microsoft/trocr-base-stage1")

uploaded_file = st.file_uploader("Sube una imagen", type=["jpg","png","jpeg"])
if uploaded_file:
    image = Image.open(uploaded_file).convert("RGB")
    pixel_values = processor(images=image, return_tensors="pt").pixel_values
    generated_ids = model.generate(pixel_values)
    text = processor.batch_decode(generated_ids, skip_special_tokens=True)[0]
    st.write("Texto detectado:", text)
