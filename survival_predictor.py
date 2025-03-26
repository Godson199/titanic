import base64
import numpy as np
import pandas as pd
import streamlit as st
from streamlit_option_menu import option_menu
import pickle  

st.markdown(f'<h1 style="color:#33ff33; font-size:60px;">{"Wine Quality Prediction "}</h1>', unsafe_allow_html=True)

# loading model
pickle_in = open("wine_quality_model_1", "rb")
model = pickle.load(pickle_in)

def get_base64(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()


def set_background(png_file):
    bin_str = get_base64(png_file)
    page_bgr_img = '''
    <style>
    .stApp {
        background-image: url("data:image/png;base64,%s");
        background-size:cover;
    }
    </style>
    ''' % bin_str
    st.markdown(page_bgr_img, unsafe_allow_html=True)

set_background('./images/background.png')


# side_bar to navigate
with st.sidebar:
    selected = option_menu("Multiple Model Prediction",
    ["XGBoost Classifier",
    "LGBM Classifier"],
    icons=["1-circle-full", "2-circle-full", "3-circle-full"],
    default_index=0)


# making prediction with the model
def predict_wine_quality(fixed_acidity, volatile_acidity, citric_acid, residual_sugar,chlorides, free_sulfur_dioxide, total_sulfur_dioxide, density,pH, sulphates, alcohol, quality):

    prediction = model.predict(np.array([[fixed_acidity, volatile_acidity, citric_acid, residual_sugar, chlorides, free_sulfur_dioxide, total_sulfur_dioxide, density,pH, sulphates, alcohol, quality]], dtype=object))
    return prediction
def main():
# building interface with streamlit
    if (selected == "XGBoost Classifier"):
        col1, col2, col3, col4 = st.columns(4)

        with col1:
            fixed_acidity = st.text_input("fixed acidity", "")
        with col2:
            volatile_acidity = st.text_input("volatile acidity", "")

        with col3:
            citric_acid = st.text_input("citric acid.5", "")
        
        with col4:
            residual_sugar = st.text_input("residual sugar.5", "")
        
        with col1:
            chlorides = st.text_input("chlorides", "")
        
        with col2:
            free_sulfur_dioxide = st.text_input("free sulfur dioxide", "")
        
        with col3:
            total_sulfur_dioxide = st.text_input("total sulfur dioxide", "")

        with col4:
            density = st.text_input("density", "")

        with col1:
            pH = st.text_input("pH", "")
        with col2:
            sulphates = st.text_input("sulphates", "")
        with col3:
            alcohol = st.text_input("alcohol", "")
        with col4:
            quality = st.text_input("quality", "")

        result=""
        if st.button("Wine Quality"):
            result = predict_wine_quality(Temperature,Relative_Humidity,Sensor1_PM2_5,Sensor2_PM2_5,Datetime_month,Datetime_year, Datetime_hour,Datetime_day)

            if result == 1:
                st.success("Good Wine Quality ")
            else:
                st.success("Bad Wine Quality!")
    
    # Next Model

    
    if st.button("About"):
        st.text("Built by: Izuogu Chibuzor Godson")


if __name__== "__main__":
    main()