import streamlit as st
from bmi import constant


def main():
    st.title("Welcome to BMI Calculator")

    html_temp = """
	

    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Know Your BMI In One Click</h2>

    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)

    page_bg_img = '''
      <style>
 	body {
	background-image: url("https://user-images.githubusercontent.com/53088237/103136369-c286c780-46e5-11eb-95b6-3a8d4a59a14b.jpg");
	background-size: cover;
	}
	</style>
	'''

#    st.markdown(page_bg_img, unsafe_allow_html=True)

    weight = st.number_input("Enter your weight (in kgs)")

    status = st.radio('Select your height format: ',
                      ('cms', 'meters', 'feet'))

    if (status == 'cms'):
        # take height input in centimeters
        height = st.number_input('Centimeters')

        try:
            bmi = weight / ((height / 100) ** 2)
        except:
            st.text("Enter some value of height")

    elif (status == 'meters'):
        # take height input in meters
        height = st.number_input('Meters')

        try:
            bmi = weight / (height ** 2)
        except:
            st.text("Enter some value of height")

    else:
        # take height input in feet
        height = st.number_input('Feet')

        # 1 meter = 3.28
        try:
            bmi = weight / (((height / 3.28)) ** 2)
        except:
            st.text("Enter some value of height")

        # check if the button is pressed or not
    if (st.button('Calculate BMI')):

        # print the BMI INDEX
        st.text("Your BMI Index is {}.".format(bmi))

        # give the interpretation of BMI index
        if (bmi < 16):
            st.error("You are Extremely Underweight")
        elif (bmi >= 16 and bmi < 18.5):
            st.warning("You are Underweight")
        elif (bmi >= 18.5 and bmi < 25):
            st.success("Healthy")
        elif (bmi >= 25 and bmi < 30):
            st.warning("Overweight")
        elif (bmi >= 30):
            st.error("Extremely Overweight")

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

