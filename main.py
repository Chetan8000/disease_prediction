from breast_cancer.breast_cancer import main as breast_cancer
from diabetes.diabetes import main as diabetes
from bmi.bmi import main as b
from heart.heart import main as heart
import streamlit as st
from multiapp import MultiApp

'''
Created on Wed December 16
@author: Chetan Borse
'''

app = MultiApp()

app.add_app("BMI",b)
app.add_app("Diabetes Prediction", diabetes)
app.add_app("Heart Disease Prediction", heart)
app.add_app("Breast Cancer Prediction", breast_cancer)


app.run()

