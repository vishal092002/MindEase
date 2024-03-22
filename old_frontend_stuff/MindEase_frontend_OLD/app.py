from flask import Flask, render_template, request, redirect, url_for
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Make a POST request to the backend login endpoint
        backend_url = "http://127.0.0.1:8000/login"  # Update with your backend URL
        payload = {'username': username, 'password': password}
        response = requests.post(backend_url, json=payload)

        # Check the response from the backend
        if response.status_code == 200:
            return f'Welcome, {username}!'
        elif response.status_code == 401:
            return 'Invalid password'
        elif response.status_code == 404:
            return 'User not found'
        else:
            return 'An error occurred while processing your request'

    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form['email']
        username = request.form['username']
        password = request.form['password']
        confirm_password = request.form['confirm_password']

        # Make a POST request to the backend register endpoint
        backend_url = "http://127.0.0.1:8000/register"  # Update with your backend URL
        payload = {
            'email': email,
            'username': username,
            'password': password,
            'confirm_password': confirm_password
        }
        response = requests.post(backend_url, json=payload)

        # Check the response from the backend
        if response.status_code == 200:
            return redirect(url_for('login'))  # Redirect to login page if registration is successful
        elif response.status_code == 400:
            return 'Username, password, and email are required'
        elif response.status_code == 409:
            return 'User already exists'
        else:
            return 'An error occurred while processing your request'

    return render_template('register.html')

if __name__ == '__main__':
    app.run(debug=True, port=5000)
