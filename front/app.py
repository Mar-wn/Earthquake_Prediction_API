import streamlit as st
import requests


st.title('Blood Donation prediction')


features_form = st.form(key= 'features_form')

months_since_first = features_form.number_input('Months since first donation:',
                         value= 0.0,
                         min_value= 0.0,
                         step= 0.5,
                         format= '%.2f')

months_since_last = features_form.number_input('Months since last donation:',
                         value= 0.0,
                         min_value= 0.0,
                         step= 0.5,
                         format= '%.2f')

number_of_donations = features_form.number_input('Number of donations:',
                         value= 0,
                         min_value= 0,
                         step= 1)

total_blood_donated = features_form.number_input('Total blood donated(in Liters):',
                         value= 0.0,
                         min_value= 0.0,
                         step= 0.1,
                         format= '%.3f')


if features_form.form_submit_button('predict'):

    url = 'https://api-izmj.onrender.com/predict' #to replace with service name when its possible to have a private network for services

    data = {
                "months_since_first": months_since_first,
                "months_since_last": months_since_last,
                "number_of_donations": number_of_donations,
                "total_blood_donated": total_blood_donated
                }

    response = requests.post(url, json= data)

    if response.status_code == 200:

        if response.text.replace('"', '') == '1':

            st.write("That's a donor! You should call him now!")

        else:

            st.write("This person is unlikely to donate blood now, please proceed to the next prospects.")

    else:

        st.write('Prediction error: {}'.format(response.text))

       