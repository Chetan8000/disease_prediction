import joblib
import numpy as np
import streamlit as st
import webbrowser
from heart import constant

PKLPath = 'heart/heart_model.pkl'


def ValuePredictor(to_predict, size):
    '''	Chest Pain Type
        Resting Blood Pressure (in mm Hg)
        Serum Cholestoral in mg/dl
        Fasting Blood Sugar
        Resting Electro-cardiographic Result
        Maximum Heart Rate Achieved
	Exercise Induced Angina
    '''
    if (size == 7):
        loaded_model = joblib.load(PKLPath)
        result = loaded_model.predict(to_predict)
    return result[0]

def main():
    #st.title("Know Your Chances Of Getting Heart Disease In One Click!")
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Know Your Chances Of Getting Heart Disease In One Click! </h2>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)

    page_bg_img = '''
      <style>
 	body {
	background-image: url("https://user-images.githubusercontent.com/53088237/103136207-5ce60b80-46e4-11eb-983e-d0fd7cb7f01b.jpg");
	background-size: cover;
	}
	</style>
	'''

#    st.markdown(page_bg_img, unsafe_allow_html=True)
    chest_status = st.radio('Chest Pain Type', ('Typical Angina', 'Atypical Angina', 'Non-Anginal Pain', 'Asymptomatic'))
    pain_limit = 0
    if (chest_status == 'Typical Angina'):
        pain_limit = 1
    elif (chest_status == 'Atypical Angina'):
        pain_limit = 2
    elif (chest_status == 'Non-Anginal Pain'):
        pain_limit = 3
    elif (chest_status == 'Asymptomatic'):
        pain_limit = 4
	

    bp = st.number_input("Resting Blood Pressure (in mm Hg)")


    serum_cholestrol = st.number_input("Serum Cholestoral in mg/dl")


    fasting_bs = st.radio('Fasting Blood Sugar', ('Fasting Blood Sugar < 120 mg/dl', 'Fasting Blood Sugar > 120 mg/dl'))
    blood_sugar = 0
    if (fasting_bs == 'Fasting Blood Sugar < 120 mg/dl'):
        blood_sugar = 0
    elif (fasting_bs == 'Fasting Blood Sugar > 120 mg/dl'):
        blood_sugar = 1



    ec_result = st.radio('Resting Electro-cardiographic Result', ('Normal', 'Having ST-T wave Abnormality', 'Showing Probable or Definite Left Ventricular Hypertrophy'))
    ecr = 0
    if (ec_result == 'Normal'):
        ecr = 0
    elif (ec_result == 'Having ST-T wave Abnormality'):
        ecr = 1
    elif (ec_result == 'Showing Probable or Definite Left Ventricular Hypertrophy'):
        ecr = 2

    mhr = st.number_input("Maximum Heart Rate Achieved")


    eia_status = st.radio('Exercise Induced Angina', ('Yes', 'No'))
    eia = 0
    if (eia_status == 'Yes'):
        eia = 1
    elif (fasting_bs == 'No'):
        eia = 0


    to_predict_list = [pain_limit, bp, serum_cholestrol, blood_sugar, ecr, mhr, eia ]
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
        webbrowser.open_new_tab("https://en.wikipedia.org/wiki/Cardiovascular_disease")

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




