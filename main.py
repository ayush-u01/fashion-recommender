import streamlit as st
import os
from PIL import Image
import numpy as np
import pickle
# import tensorflow
from sklearn.neighbors import NearestNeighbors
from numpy.linalg import norm


st.title('Fashion Recommender System')

def save_uploaded_file(uploaded_file):
    try:
        with open(os.path.join('uploads',uploaded_file.name),'wb') as f:
            f.write(uploaded_file.getbuffer())
        return 1
    except:
        return 0


# steps
# file upload -> save
uploaded_file = st.file_uploader("Choose an image")
if uploaded_file is not None:
    if save_uploaded_file(uploaded_file):
        # display the file
        display_image = Image.open(uploaded_file)
        st.image(display_image)
        # feature extract
        # features = feature_extraction(os.path.join("uploads",uploaded_file.name),model)
        #st.text(features)
        # recommendention
        # indices = recommend(features,feature_list)
        # show

        # col1,col2,col3,col4,col5 = st.beta_columns(5)

        # with col1:
        #     st.image(filenames[indices[0][0]])
        # with col2:
        #     st.image(filenames[indices[0][1]])
        # with col3:
        #     st.image(filenames[indices[0][2]])
        # with col4:
        #     st.image(filenames[indices[0][3]])
        # with col5:
        #     st.image(filenames[indices[0][4]])
    
    
    else:
        st.header("Some error occured in file upload")
