# Coding UI

# Import Statements
import streamlit as st
from streamlit_option_menu import option_menu
import PredictFunction
import pyautogui
import os
# key1 = "ctrl"
# key2 = "r"
print()
Search_text_array = []

symptomList = ['Itching', 'Skin Rash', 'Nodal Skin Eruptions', 'Continuous Sneezing', 'Shivering', 'Chills', 'Joint Pain', 'Stomach Pain', 'Acidity', 'Ulcers On Tongue', 'Muscle Wasting', 'Vomiting', 'Burning Micturition', 'Spotting  urination', 'Fatigue', 'Weight Gain', 'Anxiety', 'Cold Hands And Feets', 'Mood Swings', 'Weight Loss', 'Restlessness', 'Lethargy', 'Patches In Throat', 'Irregular Sugar Level', 'Cough', 'High Fever', 'Sunken Eyes', 'Breathlessness', 'Sweating', 'Dehydration', 'Indigestion', 'Headache', 'Yellowish Skin', 'Dark Urine', 'Nausea', 'Loss Of Appetite', 'Pain Behind The Eyes', 'Back Pain', 'Constipation', 'Abdominal Pain', 'Diarrhoea', 'Mild Fever', 'Yellow Urine', 'Yellowing Of Eyes', 'Acute Liver Failure', 'Swelling Of Stomach', 'Swelled Lymph Nodes', 'Malaise', 'Blurred And Distorted Vision', 'Phlegm', 'Throat Irritation', 'Redness Of Eyes', 'Sinus Pressure', 'Runny Nose', 'Congestion', 'Chest Pain', 'Weakness In Limbs', 'Fast Heart Rate', 'Pain During Bowel Movements', 'Pain In Anal Region', 'Bloody Stool', 'Irritation In Anus', 'Neck Pain', 'Dizziness', 'Cramps', 'Bruising', 'Obesity', 'Swollen Legs', 'Swollen Blood Vessels', 'Puffy Face And Eyes', 'Enlarged Thyroid', 'Brittle Nails', 'Swollen Extremeties', 'Excessive Hunger', 'Extra Marital Contacts', 'Drying And Tingling Lips', 'Slurred Speech', 'Knee Pain', 'Hip Joint Pain', 'Muscle Weakness', 'Stiff Neck', 'Swelling Joints', 'Movement Stiffness', 'Spinning Movements', 'Loss Of Balance', 'Unsteadiness', 'Weakness Of One Body Side', 'Loss Of Smell', 'Bladder Discomfort', 'Foul Smell Of urine', 'Continuous Feel Of Urine', 'Passage Of Gases', 'Internal Itching', 'Toxic Look (typhos)', 'Depression', 'Irritability', 'Muscle Pain', 'Altered Sensorium', 'Red Spots Over Body', 'Belly Pain', 'Abnormal Menstruation', 'Dischromic  Patches', 'Watering From Eyes', 'Increased Appetite', 'Polyuria', 'Family History', 'Mucoid Sputum', 'Rusty Sputum', 'Lack Of Concentration', 'Visual Disturbances', 'Receiving Blood Transfusion', 'Receiving Unsterile Injections', 'Coma', 'Stomach Bleeding', 'Distention Of Abdomen', 'History Of Alcohol Consumption', 'Fluid Overload', 'Blood In Sputum', 'Prominent Veins On Calf', 'Palpitations', 'Painful Walking', 'Pus Filled Pimples', 'Blackheads', 'Scurring', 'Skin Peeling', 'Silver Like Dusting', 'Small Dents In Nails', 'Inflammatory Nails', 'Blister', 'Red Sore Around Nose', 'Yellow Crust Ooze']
Symptoms = sorted(symptomList)
Symptoms = Symptoms
# Loading the saved Models

Side_bar = ['Home', 'Know your Disease', 'Prediction History']

# Main Heading
st.header('**Disease Prediction Using ML**')

# Sidebar to Navigate
with st.sidebar:
    selected = option_menu('Disease Prediction', Side_bar, icons=['house-fill', 'activity', 'clock-history'],
                           default_index=1)

if selected == Side_bar[0]:
        st.image('C:/Users/Karth/PycharmProjects/Disease Prediction/HomeScreenImage.svg')
        st.text("Created By Yash Patel, Kartikheyaa Kurra, Nethra Balaraman")
# Predicting a Disease through Symptom Analysis
if selected == Side_bar[1]:
    st.text('*Disclaimer*')
    st.text("*This prediction shouldn't be taken as gospel, please consult a doctor.*")
    st.title('Symptoms')
    # Creating the Search Bar
    # Search_text=st.text_input("", placeholder='Search...')

    # Search_text_array.append((Search_text))
    col1, col2, col3 = st.columns(3)



    CheckBoxes = []
    selected_checkbox = []

    with col1:
        with col1:
            for i in range(0, 44):
                # if Search_text == Symptoms[i]:
                #     Column1 = st.checkbox(Symptoms[i], key=Symptoms[i], value=True)
                # else:
                Column1 = st.checkbox(Symptoms[i], key=Symptoms[i], value=False)
                CheckBoxes.append(Column1)
                if Column1:
                    selected_checkbox.append(Symptoms[i])
            submitButton = st.button('Submit')
    with col2:
        for i in range(45, 88):
        #     if Search_text == Symptoms[i]:
        #         Column2 = st.checkbox(Symptoms[i], key=Symptoms[i], value=True)
        #     else:
            Column2 = st.checkbox(Symptoms[i], key=Symptoms[i], value=False)
            CheckBoxes.append(Column2)
            if Column2:
                selected_checkbox.append(Symptoms[i])
    with col3:
        for i in range(88, 131):
            # if Search_text == Symptoms[i]:
            #     Column3 = st.checkbox(Symptoms[i], key=Symptoms[i], value=True)
            # else:
            Column3 = st.checkbox(Symptoms[i], key=Symptoms[i], value=False)
            CheckBoxes.append(Column3)
            if Column3:
                selected_checkbox.append(Symptoms[i])
        i = 44
        Column3 = st.checkbox(Symptoms[i])
        CheckBoxes.append(Column3)
        if Column3:
            selected_checkbox.append((Symptoms[i]))
        clearButton = st.button('Clear')

    symptom_index = 0


    if submitButton:
        y = str(selected_checkbox)
        x = PredictFunction.predictdisease(selected_checkbox)
        st.text("Your Symptoms: " + y)
        st.text(x)
        f = open('C:/Users/Karth/PycharmProjects/Disease Prediction/historyData.txt', 'a')
        line = '- Symptoms: ' + y + ' = ' + x
        f.write(line)
        f.write('\n')
        # PrevHistory.update()

    if clearButton:
        pyautogui.hotkey('ctrl', 'r')

if selected == Side_bar[2]:
    f = open('C:/Users/Karth/PycharmProjects/Disease Prediction/historyData.txt', 'r')
    raw_text = str(f.read())
    st.write(raw_text)
    clearHistory = st.button('Clear History')
    if clearHistory:
        del f
        os.remove('C:/Users/Karth/PycharmProjects/Disease Prediction/historyData.txt')
        f = open('C:/Users/Karth/PycharmProjects/Disease Prediction/historyData.txt', "w+")
        pyautogui.hotkey('ctrl', 'r')

# print(CheckBoxes)