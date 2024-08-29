import streamlit as st
import cv2 as cv
from PIL import Image
import numpy as np
from image_processing import image_preprocessing
from prediction import get_prediction

st.write("Number Plate Character Segmentation And Recognition")

image_file = st.file_uploader("Please Upload an image of a number plate. Note: The image should be a cropped image of plates only")

if image_file:
    
    image_final = Image.open(image_file)
    st.image(image_final)

    image_array = np.array(image_final)

    prediction, bbox, contrast= get_prediction(image_array)
    st.image(contrast)
    st.image(bbox)


    st.write(prediction)






