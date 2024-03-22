import streamlit as st

# Function to logout the user
def logout():
    st.session_state.logged_in = False
    st.session_state.username = None
    st.info("You have been logged out.")