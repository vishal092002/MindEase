import streamlit as st 
import sqlite3

# Function to display the registration page
def register_page():
    st.title("Register")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    confirm_password = st.text_input("Confirm Password", type="password")
    email = st.text_input("Email")
    if st.button("Register"):
        if password == confirm_password:
            register(username, password, email)
        else:
            st.error("Passwords do not match.")

# Function to register a new user
def register(username, password, email):
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    try:
        c.execute('INSERT INTO users (username, password, email) VALUES (?, ?, ?)', (username, password, email))
        conn.commit()
        st.success("Registration successful. Please login.")
    except sqlite3.IntegrityError:
        st.error("Username or email already exists. Please choose a different one.")
    conn.close()