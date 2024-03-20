import streamlit as st 
import sqlite3

# Function to logout the user
def logout():
    st.session_state.logged_in = False
    st.session_state.username = None
    st.info("You have been logged out.")