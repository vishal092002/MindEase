import streamlit as st
import sqlite3

# Function to authenticate a user
def login(username_or_email, password):
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute('SELECT * FROM users WHERE (username=? OR email=?) AND password=?', (username_or_email, username_or_email, password))
    user_data = c.fetchone()
    conn.close()
    if user_data:
        st.session_state.logged_in = True
        st.session_state.username = user_data[1]
        st.success(f"Welcome back, {user_data[1]}!")
    else:
        st.error("Invalid username/email or password.")

# Function to display the login page with LLM chatbot
def login_page():
    st.title("Login")
    username_or_email = st.text_input("Username/Email")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        login(username_or_email, password)