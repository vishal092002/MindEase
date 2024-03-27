from flask import Flask, render_template, request, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy
import requests
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)
'''
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# TODO: For testing purposes - removed the unique aspect
class Client(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120),  nullable=False)
    username = db.Column(db.String(80),  nullable=False)
    password = db.Column(db.String(80), nullable=False)

class Therapist(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), nullable=False)
    username = db.Column(db.String(80), nullable=False)
    password = db.Column(db.String(80), nullable=False)
    
# Create users table if not exists
with app.app_context():
    db.create_all()
'''
@app.route('/')
def home():
    return render_template('home.html')

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

@app.route('/register_client', methods=['GET', 'POST'])
def register_client():
     if request.method == 'POST':
        email = request.form['email']
        username = request.form['username']
        password = request.form['password']
        confirm_password = request.form['confirm_password']

        # Make a POST request to the backend register endpoint
        backend_url = "http://127.0.0.1:8000/register_client"  # Update with your backend URL
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

     return render_template('register_client.html')  

@app.route('/register_therapist', methods=['GET', 'POST'])
def register_therapist():
    if request.method == 'POST':
        email = request.form['email']
        username = request.form['username']
        password = request.form['password']
        confirm_password = request.form['confirm_password']
        resume = request.files['resume']

        if resume:
            filename = secure_filename(resume.filename)
        else:
            return 'Resume file is required'

        # Make a POST request to the backend register_therapist endpoint
        backend_url = "http://127.0.0.1:8000/register_therapist"  # Update with your backend URL
        payload = {
            'email': email,
            'username': username,
            'password': password,
            'confirm_password': confirm_password,
            'resume': filename  # Sending the filename to the backend
        }
        response = requests.post(backend_url, json=payload)

        # Check the response from the backend
        if response.status_code == 200:
            return redirect(url_for('login'))  # Redirect to login page if registration is successful
        elif response.status_code == 400:
            return 'Username, password, email, and resume are required'
        elif response.status_code == 409:
            return 'User already exists'
        else:
            return 'An error occurred while processing your request'

    return render_template('register_therapist.html')

@app.route('/profile/<username>')
def profile(username):
    return render_template('profile.html', username=username)

@app.route('/aboutus')
def aboutus():
    return render_template('aboutus.html')

if __name__ == '__main__':
    app.run(debug=True)
