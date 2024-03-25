from flask import request, jsonify, current_app, g
from werkzeug.security import generate_password_hash, check_password_hash

def get_db():
    if 'db' not in g:
        # Use the database connection stored in the application context
        g.db = current_app.config['DB_CONNECTION'].cursor(dictionary=True)
    return g.db

def close_db(e=None):
    # Close the database connection when the request is finished
    db = g.pop('db', None)
    if db is not None:
        db.close()

def user_exists(email):
    db = get_db()
    db.execute("SELECT id FROM users WHERE email = %s", (email,))
    return db.fetchone() is not None

def login():
    with current_app.app_context():
        # Get user input from request
        name = request.json.get('username')
        password = request.json.get('password')

        # Check if email and password are provided
        if not name or not password:
            return jsonify({"error": "Username and password are required"}), 400

        try:
            # Get database cursor
            db = get_db()

            # Check if the user exists and retrieve the stored hashed password
            db.execute("SELECT password FROM users WHERE name = %s", (name,))
            stored_password = db.fetchone()

            if stored_password:
                # User exists, check the password
                if check_password_hash(stored_password['password'], password):
                    return jsonify({"message": "Login successful"})
                else:
                    return jsonify({"error": "Invalid password"}), 401
            else:
                return jsonify({"error": "User not found"}), 404

        except Exception as e:
            print(f"Error: {e}")
            return jsonify({"error": "Database error"}), 500

def register_client():
    # Get user input from request
    name = request.json.get('username')
    password = request.json.get('password')
    email = request.json.get('email')

    # Check if username, password, and email are provided
    if not name or not password or not email:
        return jsonify({"error": "Username, password, and email are required"}), 400

    try:
        # Get database cursor
        db = get_db()

        # Check if the user already exists
        if user_exists(email):
            return jsonify({"error": "User already exists"}), 409

        # Hash the password before storing it in the database
        hashed_password = generate_password_hash(password, method='pbkdf2:sha256')

        # Insert the new user into the database with hashed password
        db.execute("INSERT INTO users (name, password, email) VALUES (%s, %s, %s)", (name, hashed_password, email))
        current_app.config['DB_CONNECTION'].commit()

        return jsonify({"message": "User successfully registered"})

    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"error": "Database error"}), 500

# Register close_db to be called after each request
current_app.teardown_appcontext(close_db)
