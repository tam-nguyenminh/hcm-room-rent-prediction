import streamlit as st

pg = st.navigation([
    st.Page(page="streamlit_prediction_page.py", title='Prediction', icon=':material/experiment:'), 
    st.Page(page='pages/About.py', title='About Dataset', icon=':material/info:', url_path='About-info')
    ])
pg.run()
