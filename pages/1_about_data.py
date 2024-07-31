import streamlit as st
import pandas as pd, numpy as np
import seaborn as sns, matplotlib.pyplot as plt

def show_about_page():
    st.title('Room for Rent Price Prediction')
    st.header('Ho Chi Minh city',divider='rainbow')

    st.subheader('Model used in the learning process')
    st.markdown('Linear Regression')
    st.markdown('Random Forest')
    st.markdown('Drawback: data information such as furniture, room status etc., facility neighborhood is not provided.')

show_about_page()

def import_data():
    df = pd.read_csv('hcm_room_for_rent_cleaned_v2.csv')
    df = df.sort_values('district', ascending=True)
    return df

df = import_data()
df['square_meter'] = df['acreage']

# st.write(df)


def plot_box():
    fig, ax = plt.subplots()
    plt.figure(figsize=(15,10))
    sns.boxplot(df, y='district',x='price', ax=ax, palette='viridis')
    return fig 

st.subheader('Price distribution per district')
plot_price_per_district = plot_box()
st.pyplot(plot_price_per_district)

st.subheader('Price and square_meter')


def plot_price_meter(df):
    st.scatter_chart(df, x='square_meter', y='price', size='price', color='district')
# create slider of square metre
st.markdown('Select a district.')
dist_list = df.district.unique()
dist_slt = st.selectbox(f'Now select a district', dist_list)
df_district = df[df['district'] ==dist_slt]


plot_price_meter(df_district)



