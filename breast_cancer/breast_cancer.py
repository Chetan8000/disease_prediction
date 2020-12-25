import joblib
import numpy as np
from breast_cancer import constant
import pickle
import webbrowser
import streamlit as st

PKLPath = 'breast_cancer/cancer_model.pkl'

def ValuePredictor(to_predict, size):
    '''	Mean of the Concave Points
        Mean of the Area
        Mean of the Radius
        Mean of the Perimeters
        Mean of the Concavity
    '''
    if (size == 5):
        loaded_model = joblib.load(PKLPath)
        result = loaded_model.predict(to_predict)
    return result[0]


def main():
    st.title("Know Your Chances Of Getting Breast Cancer In One Click!")
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Know Your Chances Of Getting Breast Cancer In One Click! </h2>
    </div>
    """

    st.markdown(html_temp, unsafe_allow_html=True)
    cp = st.number_input("Mean of the Concave Points")
    area = st.number_input("Mean of the Area")
    radius = st.number_input("Mean of the Radius")
    perimeters = st.number_input("Mean of the Perimeters")
    concavity = st.number_input("Mean of the Concavity")
    to_predict_list = [cp, area, radius, perimeters, concavity]
    size = len(to_predict_list)
    result = ""
    prediction = ""
    if st.button("Predict"):
        to_predict = np.array(to_predict_list).reshape(1, size)
        result = ValuePredictor(to_predict, size)
        if int(result) == 1:
            prediction = "Sorry you chances of getting the disease. Please consult the doctor immediately"
        else:
            prediction = "No need to fear. You have no dangerous symptoms of the disease"

    st.success(prediction)
    if st.button("About Diabetes"):
        webbrowser.open_new_tab("https://en.wikipedia.org/wiki/Breast_cancer")

    info_about = '''
    <div id="footer" class="text-center center-block">
          <p>© 2020 Author: Chetan Borse</p>
    </div>
    '''
    st.markdown(info_about, unsafe_allow_html=True)

    html = f"""<div
    <ul class="mylinks">
	<a href='https://github.com/Chetan8000/'><img src='data:image/png;base64,{constant.Github}'></a>
        <a href='https://www.linkedin.com/in/borsechetan800/'><img src='data:image/png;base64,{constant.LinkedIN}'></a>
    </ul>    </div>"""
    st.markdown(html, unsafe_allow_html=True)


