import streamlit as st 
from time import sleep
from stqdm import stqdm
import pandas as pd
from transformers import pipeline
import json
import spacy
import spacy_streamlit


def draw_all( key, plot=False, ):
    st.write(
        """
        # this is Fashion Recommendation Web App
        
        This Web App can do anything u can imagine. 😱 
        
        This App is built using pretrained transformers which are capable of doing wonders with the images.
        
        ```python
        # Key Features of this App.
        1. lorem32
        2. lorem32
        3. lorem32
        4. lorem32
        5. lorem32
       
        ```
        """
    )



with st.sidebar:
    draw_all("sidebar")



def main():
    st.title(" Fashion Recommendation Web App")
       
  

if __name__ == '__main__':
	main()
