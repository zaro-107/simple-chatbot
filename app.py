import pandas as pd
import numpy as np
import pickle as pk
import streamlit as st

model = pk.load(open('model.pkl','rb'))
st.header('Car price prediction Ml Model')
car_data = pd.raed_csv('car data - Copy.csv')

def get_brand_name(car_name):
    car_name = car_name.split(" ")[0]
    return car_name.strip()
car_data['Car_name'] = car_data['Car_name'].apply(get_brand_name)
name=st.slectbox = ('Select Car Brand',car_data[Car_name])
year=st.slider('car manufactured year',2000,2019)
km_driven=st.slider('No.of kms driven',11,200000)
fuel=st.selectbox('Fuel type',car_data['Fuel_Type'].unique())
owner=st.selectbox('seler type',car_data['Seller_Type'].unique())
transmission=st.selectbox('Transmission',car_data['transmisson'].unique())
seats=st.slider('NO. of seats',5,10)


if st.button("Predict"):
    input_data_model = pd.DataFrame({
    'Year': [Year],
    'Present_Price': [Present_Price],
    'Kms_Driven': [Kms_Driven],
    'Fuel_Type': [Fuel_Type],
    'Seller_Type': [],
    'Transmission': [Transmission],
    'Owner': [Owner],
    'car_name': [car_name]
})
st.write(input_data_model)

