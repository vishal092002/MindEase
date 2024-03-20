import streamlit as st 
import sqlite3

# make a POST function for the backend
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
    
# POST for register to back
# import requests

# # Define the backend URL
# backend_url = 'http://your-backend-url/api/register'

# # Define the user data to be sent in the POST request
# user_data = {
#     'username': 'example_user',
#     'password': 'example_password',
#     'email': 'example@example.com'
# }

# # Send a POST request to the backend
# response = requests.post(backend_url, json=user_data)

# # Check the response status code and content
# if response.status_code == 200:
#     print('Registration successful. Please login.')
# elif response.status_code == 400:
#     print('Bad request. Please check your data.')
# elif response.status_code == 409:
#     print('Username or email already exists. Please choose a different one.')
# else:
#     print('Error:', response.text)

# This code is a skeleton for using POSTMAN to POST to the backend
# import requests

# # Define the backend URL
# backend_url = 'http://your-backend-url/api/register'

# # Define the user data to be sent in the POST request
# user_data = {
#     'username': 'example_user',
#     'password': 'example_password',
#     'email': 'example@example.com'
# }

# # Send a POST request to the backend using requests
# response = requests.post(backend_url, json=user_data)

# # Check the response status code and content
# if response.status_code == 200:
#     print('Registration successful. Please login.')
# elif response.status_code == 400:
#     print('Bad request. Please check your data.')
# elif response.status_code == 409:
#     print('Username or email already exists. Please choose a different one.')
# else:
#     print('Error:', response.text)
