


import streamlit as st
from img_classification import seecraft_classification
from PIL import Image


st.title("Image Classification with SeeCraft")
st.header("Detecting Seacraft Example")
st.text("Upload an Image to be classified as 'Ship Absent' or 'Ship Present'")


uploaded_file = st.file_uploader("Choose a satellite image ...", type="jpg")

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image.', use_column_width=True)
    st.write("")
    st.write("Classifying...")
    label = seecraft_classification(image, '')
    if label == 0:
        st.write("Ship Absent: The image does not contain a ship.")
    else:
        st.write("Ship Present: The image contains a ship!")
