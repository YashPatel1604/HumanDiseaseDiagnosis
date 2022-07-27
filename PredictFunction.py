import streamlit
from keras.models import load_model
import numpy as np
from scipy.stats import mode
import pickle

nb = pickle.load(open('C:/Users/Karth/PycharmProjects/Disease Prediction/Saved Models'
                      '/DiseaseDetectiongaussian_NB_model.sav', 'rb'))
rf = pickle.load(open('C:/Users/Karth/PycharmProjects/Disease Prediction/Saved Models/DiseaseDetectionrf_model.sav',
                      'rb'))
svm = pickle.load(open('C:/Users/Karth/PycharmProjects/Disease Prediction/Saved Models/DiseaseDetectionsvm_model.sav',
                       'rb'))
encoder = load_model('C:/Users/Karth/PycharmProjects/Disease Prediction/DiseaseDetectionEncoder.sav', 'rb')


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
encoder(symptomList)
symptoms = symptomList
# Creating a symptom index dictionary to encode the
# input symptoms into numerical form
symptom_index = {}
for index, value in enumerate(symptoms):
    symptom = "".join(value)
    symptomList[index] = symptom
    symptom_index[symptom] = index

data_dict = {
    "symptom_index": symptom_index,
    "predictions_classes": encoder.classes_
}
streamlit.text(print(data_dict))
# Defining the Function
# Input: string containing symptoms separated by commmas
# Output: Generated predictions by models


def predictdisease(symptoms):

    # symptoms = symptoms.split(",")
    # creating input data for the models
    input_data = [0] * len(data_dict["symptom_index"])
    for symptom in symptoms:
        index = data_dict["symptom_index"][symptom]
        input_data[index] = 1

    # reshaping the input data and converting it
    # into suitable format for model predictions
    input_data = np.array(input_data).reshape(1, -1)

    # generating individual outputs
    rf_prediction = data_dict["predictions_classes"][rf.predict(input_data)[0]]
    nb_prediction = data_dict["predictions_classes"][nb.predict(input_data)[0]]
    svm_prediction = data_dict["predictions_classes"][svm.predict(input_data)[0]]

    # making final prediction by taking mode of all predictions
    final_prediction = mode([nb_prediction])[0][0]
    predictions = {
        "rf_model_prediction": rf_prediction,
        "naive_bayes_prediction": nb_prediction,
        "svm_model_prediction": nb_prediction,
        "Detected Disease": final_prediction
    }
    return predictions



