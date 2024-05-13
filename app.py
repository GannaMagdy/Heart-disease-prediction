import streamlit as st 
import pickle
import pandas as pd


st.title('Heart Prediction app')
st.info('Application for Heart Disease Predection')
st.sidebar.header('Feature Selection')

Age=st.text_input('Age')
Sex=st.text_input('Sex')
BP=st.text_input('BP')
Cholesterol=st.text_input('Cholesterol')
Thallium=st.text_input('Thallium')
Chest_pain_type=st.text_input('Chest pain type')
EKG_results=st.text_input('EKG results')
Exercise_angina=st.text_input('Exercise angina')
ST_depression=st.text_input('ST depression')
FBS_over_120=st.text_input('FBS over 120')
Max_HR=st.text_input('Max HR')
Slope_of_ST=st.text_input('Slope of ST')
Number_of_vessels_fluro=st.text_input('Number of vessels fluro')


df=pd.DataFrame({'Age':[Age],'Sex':[Sex],
'BP':[BP], 'Cholesterol':[Cholesterol],
'Thallium':[Thallium],'Chest pain type':[Chest_pain_type],'EKG results':[EKG_results],
'Exercise angina':[Exercise_angina],'ST depression':[ST_depression],'FBS over 120':[FBS_over_120],'Max HR':[Max_HR],'Slope of ST':[Slope_of_ST],'Number of vessels fluro':[Number_of_vessels_fluro]
},index=[0])

model=pickle.load(open(r"C:\Users\janna\Downloads\Heart_disease_prediction.sav",'rb'))
Con=st.sidebar.button('confirm')
if Con:
    result=model.predict(df)
    if result == 0:
        st.sidebar.write('no risk if heart disease')
        st.sidebar.image('https://static.vecteezy.com/system/resources/previews/016/248/674/non_2x/heart-character-pose-thumb-up-vector.jpg',width=250)
    else:
        st.sidebar.write('Risk of heart disease')
        st.sidebar.image('https://cdn2.iconfinder.com/data/icons/heart-character-sticker/2608/Heart-Character-pose-so-sadly-512.png',width=250)