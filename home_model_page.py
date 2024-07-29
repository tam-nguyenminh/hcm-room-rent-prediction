import streamlit as st

# Define the page titles
PAGES = {
    "Prediction": "streamlit_prediction_page",
    "About Dataset": "About"
}

# Sidebar navigation
st.sidebar.title("Navigation")
selection = st.sidebar.radio("Go to", list(PAGES.keys()))

# Load the selected page
page = PAGES[selection]

# pg = st.navigation([
#     st.Page(page="streamlit_prediction_page.py", title='Prediction', icon=':material/experiment:'), 
#     st.Page(page='pages/About.py', title='About Dataset', icon=':material/info:', url_path='About-info')
#     ])
# pg.run()

if page == "streamlit_prediction_page":
    import pages.streamlit_prediction_page as p
    p.run()
elif page == "About":
    import pages.About as p
    p.run()
# import streamlit as st

# pg = st.navigation([
#     st.Page(page="streamlit_prediction_page.py", title='Prediction', icon=':material/experiment:'), 
#     st.Page(page='pages/About.py', title='About Dataset', icon=':material/info:', url_path='About-info')
#     ])
# pg.run()
