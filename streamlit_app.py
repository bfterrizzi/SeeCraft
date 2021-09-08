


import streamlit as st
from img_classification import seecraft_classification
from PIL import Image


st.title("SeeCraft")
st.header("AI powered ship detection in satellite imagery")
st.text("The ocean is so large enough that monitoring it from the ground is ineffective. SeeCraft provides a solution to this problem by connecting the people responsible for safeguarding our oceans to a powerful algorithm designed to detect the presence of ships in remote satellite imagery.")


uploaded_file = st.file_uploader("Choose an image to inspect...", type="jpg")

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image.', use_column_width=True)
    st.write("Studying Image...")
    st.write("Classifying...")
    label = seecraft_classification(image, '')
    if label == 0:
        st.write("Ship Absent: This image does not contain a ship.")
    else:
        st.write("Ship Present: This image contains a ship!")
