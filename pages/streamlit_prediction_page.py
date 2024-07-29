import streamlit as st
import pandas as pd
import numpy as np
import json
import pickle


st.title('Room-for-Rent Price Prediction')
st.subheader('This is to predict room renting price in Ho Chi Minh city. ', 
        help='help icon',
        divider='blue')

st.markdown('Estimator used in this training is :green[RandomForest].:sunflower:')



# import list of districts
# path = 'C:/Users/84393/OneDrive - CÔNG TY TNHH OFFICIENCE/PYTHON/ML_House_Rent/'
f = open('columns.json')
features = json.load(f)
feature_list = features['data_columns']
dist_list = features['data_columns'][1:]
# print(dist_list)

st.markdown(f'\n')

# create option list of district
st.subheader('Select a district.')
dist_slt = st.selectbox(f'Now select a district', dist_list)


# st.markdown('#')

# create slider of square metre
st.subheader('Select a square metre value.')
sqrmetre_slt = st.slider('Select an square metre value.', min_value=1, max_value=50, step=1)
st.write("Selected square metre", sqrmetre_slt)

# add model
with open(path + 'hcm_room_price_prediction_model.pickle', 'rb') as f:
    model = pickle.load(f)

def predict_price(district, sqr_meter):
    district_index = feature_list.index(district)

    x=np.zeros(len(feature_list))
    x[0]=sqr_meter
    # x[1]=bath
    if district_index >= 0:
        x[district_index] = 1
    return x.reshape(1,-1)

# print(dist_list)
# new_value = predict_price('quận 1', 45)
new_value = predict_price(dist_slt, sqrmetre_slt)

predicted_val = model.predict(new_value)[0]
# print(predicted_val)

# print(type(predicted_val))

st.subheader(f'Predicted price (million VND): ')
st.header(f':red[{predicted_val}]')
