import streamlit as st 
import sqlite3

# make a POST function for the backend
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
        
# # Function to authenticate a user - for making a postman POST to backend
# def login(username_or_email, password):
#     # Define the backend API endpoint URL
#     api_url = 'https://your-backend-api-url.com/login'
    
#     # Define the request body data (username, password)
#     data = {
#         'username_or_email': username_or_email,
#         'password': password
#     }
    
#     try:
#         # Make a POST request to the backend API
#         response = requests.post(api_url, data=data)
        
#         # Check if the request was successful (status code 200)
#         if response.status_code == 200:
#             user_data = response.json()  # Assuming the backend returns user data in JSON format
#             st.session_state.logged_in = True
#             st.session_state.username = user_data.get('username')
#             st.success(f"Welcome back, {user_data.get('username')}!")
#         else:
#             st.error("Invalid username/email or password.")
#     except requests.RequestException as e:
#         st.error(f"Error occurred: {e}")

# # Usage example
# username_or_email = st.text_input("Username/Email")
# password = st.text_input("Password", type="password")
# if st.button("Login"):
#     login(username_or_email, password)

# This code is a skeleton for using POSTMAN to POST to the backend
# import streamlit as st 
# import sqlite3
# from flask import Flask, request, jsonify

# # Initialize Flask app
# app = Flask(__name__)

# # Function to authenticate a user
# def login(username_or_email, password):
#     conn = sqlite3.connect('users.db')
#     c = conn.cursor()
#     c.execute('SELECT * FROM users WHERE (username=? OR email=?) AND password=?', (username_or_email, username_or_email, password))
#     user_data = c.fetchone()
#     conn.close()
#     if user_data:
#         return jsonify({"message": f"Welcome back, {user_data[1]}!"}), 200
#     else:
#         return jsonify({"error": "Invalid username/email or password."}), 401

# # Route for handling Postman login requests
# @app.route('/api/login', methods=['POST'])
# def postman_login():
#     data = request.get_json()
#     username_or_email = data.get('username_or_email')
#     password = data.get('password')
#     if username_or_email and password:
#         response, status_code = login(username_or_email, password)
#         return response, status_code
#     else:
#         return jsonify({"error": "Username/email and password are required."}), 400

# if __name__ == '__main__':
#     app.run(debug=True)
