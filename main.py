import streamlit as st
from streamlit_prediction_page import show_predict_page
from pages.about_page import show_about_page

pg = st.navigation([
    st.Page(page="streamlit_prediction_page.py", title='Prediction', icon=':material/experiment:'), 
    st.Page(page='pages/About_page.py', title='About Dataset', icon=':material/info:', url_path='About-info')
    ])

print(pg)
if pg.title == 'Prediction':
    show_predict_page()
else:
    show_about_page()


pg.run()
