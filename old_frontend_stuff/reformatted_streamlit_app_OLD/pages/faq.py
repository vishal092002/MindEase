import streamlit as st
from pages import logout

# Function to display the home page
def faq_page():
    st.title("FAQ Page")
    st.write("Welcome to the FAQ page.")
    st.write("CONTENT TBD")
    
    st.button("Logout", on_click=logout)