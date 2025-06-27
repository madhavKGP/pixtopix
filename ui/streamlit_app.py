import streamlit as st
import requests
from PIL import Image
import io

st.title("🛰️ Pix2Pix: Satellite to Map Image Translator")

uploaded_file = st.file_uploader("Upload a satellite image", type=["jpg", "jpeg", "png"])

if uploaded_file:
    st.image(uploaded_file, caption="Uploaded Image", use_column_width=True)

    if st.button("Generate Map"):
        files = {"file": uploaded_file.getvalue()}
        response = requests.post("http://localhost:8000/predict/", files=files)

        if response.status_code == 200:
            image = Image.open(io.BytesIO(response.content))
            st.image(image, caption="Generated Map", use_column_width=True)
        else:
            st.error("Failed to generate image.")
 