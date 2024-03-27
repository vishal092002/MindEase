from flask import Flask
import mysql.connector

app = Flask(__name__)

# Database configuration (replace these values with your actual database configuration)
db_config = {
    'host': '',
    'user': '',
    'password': '',
    'database': '',
}

# Establish database connection at the beginning
try:
    # Establish the connection
    db_connection = mysql.connector.connect(**db_config)
    app.config['DB_CONNECTION'] = db_connection

    # Notify on successful connection
    print("Successfully connected to the database!")

except mysql.connector.Error as err:
    print(f"Error: {err}")
    raise SystemExit(1)

# Register routes
with app.app_context():
    from app.routes import login, register_client, register_therapist, insert_survey 
    app.add_url_rule('/login', 'login', login, methods=['POST'])
    app.add_url_rule('/register_client', 'register_client', register_client, methods=['POST'])
    app.add_url_rule('/register_therapist', 'register_therapist', register_therapist, methods=['POST'])
    app.add_url_rule('/insert_survey', 'insert_survey', insert_survey, methods=['POST'])

if __name__ == '__main__':
    app.run(debug=True,port=8000)
