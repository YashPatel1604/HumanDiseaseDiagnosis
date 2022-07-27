# Coding UI

# Import Statements
import pickle
import streamlit as st
from streamlit_option_menu import option_menu
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.by import By
import PredictFunction

symptomList = ['Itching', 'Skin Rash', 'Nodal Skin Eruptions', 'Continuous Sneezing', 'Shivering', 'Chills',
               'Joint Pain', 'Stomach Pain', 'Acidity', 'Ulcers on Tongue', 'Muscle Wasting', 'Vomiting',
               'Burning Micturition', 'Spotting Urination', 'Fatigue', 'Weight Gain', 'Anxiety', 'Cold Hands and Feets',
               'Mood Swings', 'weight_loss', 'restlessness', 'lethargy', 'patches_in_throat', 'irregular_sugar_level',
               'cough', 'high_fever', 'sunken_eyes', 'breathlessness', 'sweating', 'dehydration', 'indigestion',
               'headache',
               'yellowish_skin', 'dark_urine', 'nausea', 'loss_of_appetite', 'pain_behind_the_eyes', 'back_pain',
               'constipation', 'abdominal_pain', 'diarrhoea', 'mild_fever', 'yellow_urine', 'yellowing_of_eyes',
               'acute_liver_failure',
               'fluid_overload', 'swelling_of_stomach', 'swelled_lymph_nodes', 'malaise',
               'blurred_and_distorted_vision',
               'phlegm', 'throat_irritation', 'redness_of_eyes', 'sinus_pressure', 'runny_nose', 'congestion'
               'chest_pain',
               'weakness_in_limbs', 'fast_heart_rate', 'pain_during_bowel_movements', 'pain_in_anal_region',
               'bloody_stool',
               'irritation_in_anus', 'neck_pain', 'dizziness',
               'cramps', 'bruising', 'obesity', 'swollen_legs', 'swollen_blood_vessels', 'puffy_face_and_eyes',
               'enlarged_thyroid', 'brittle_nails', 'swollen_extremeties', 'excessive_hunger',
               'extra_marital_contacts', 'drying_and_tingling_lips', 'slurred_speech', 'knee_pain', 'hip_joint_pain',
               'muscle_weakness', 'stiff_neck', 'swelling_joints', 'movement_stiffness',
               'spinning_movements', 'loss_of_balance', 'unsteadiness', 'weakness_of_one_body_side', 'loss_of_smell',
               'bladder_discomfort', 'foul_smell_of urine', 'continuous_feel_of_urine', 'passage_of_gases',
               'internal_itching',
               'toxic_look_(typhos)', 'depression', 'irritability', 'muscle_pain', 'altered_sensorium',
               'red_spots_over_body',
               'belly_pain', 'abnormal_menstruation', 'dischromic _patches', 'watering_from_eyes', 'increased_appetite',
               'polyuria', 'family_history', 'mucoid_sputum', 'rusty_sputum', 'lack_of_concentration',
               'visual_disturbances',
               'receiving_blood_transfusion', 'receiving_unsterile_injections', 'coma', 'stomach_bleeding',
               'distention_of_abdomen', 'history_of_alcohol_consumption', 'fluid_overload.1', 'blood_in_sputum',
               'prominent_veins_on_calf', 'palpitations', 'painful_walking', 'pus_filled_pimples', 'blackheads',
               'scurring',
               'skin_peeling', 'silver_like_dusting', 'small_dents_in_nails', 'inflammatory_nails', 'blister',
               'red_sore_around_nose', 'yellow_crust_ooze', 'prognosis']
Symptoms = sorted(symptomList)
Symptoms = Symptoms
st.text(Symptoms)
# Loading the saved Models

Side_bar = ['Home', 'Know your Disease', 'Prediction History']

# Main Heading
st.header('**Disease Prediction Using ML**')

# Sidebar to Navigate
with st.sidebar:
    selected = option_menu('Disease Prediction', Side_bar, icons=['house-fill', 'activity', 'clock-history'],
                           default_index=1)

if selected == Side_bar[0]:
    st.title('*Disclaimer*')
    st.subheader("*This prediction doesn't mean, you shouldn't consult a doctor.*")

# Predicting a Disease through Symptom Analysis
if selected == Side_bar[1]:
    st.title('Symptoms')
    # Creating the Search Bar
    Search_text = st.text_input("", placeholder='Search...')

    col1, col2, col3 = st.columns(3)

    submitButton = st.button('Submit')
    CheckBoxes = []
    selected_checkbox = []

    with col1:
        for i in range(0, 45):
            Column1 = st.checkbox(Symptoms[i])
            CheckBoxes.append(Column1)
            if Column1:
                selected_checkbox.append(Symptoms[i])
    with col2:
        for i in range(45, 90):
            Column2 = st.checkbox(Symptoms[i])
            CheckBoxes.append(Column2)
            if Column2:
                selected_checkbox.append(Symptoms[i])
    with col3:
        for i in range(90, 132):
            Column3 = st.checkbox(Symptoms[i])
            CheckBoxes.append(Column3)
            if Column3:
                selected_checkbox.append(Symptoms[i])

    # for x in CheckBoxes:
    #     if x:
    #         selected_checkbox.append(x.)

    if submitButton:
        st.text(selected_checkbox)
        st.text(PredictFunction.predictdisease(selected_checkbox))

    # for symptom in Symptoms:
    #     if Search_text == symptom:

if selected == Side_bar[2]:
    st.title('Disease Prediction History')

