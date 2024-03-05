from flask import request, jsonify, current_app, g

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
        
def user_exists(username):
    db = get_db()
    db.execute("SELECT id FROM users WHERE name = %s", (username,))
    return db.fetchone() is not None

def login():
    with current_app.app_context():
        # Get user input from request
        email = request.json.get('email')
        password = request.json.get('password')

        # Check if email and password are provided
        if not email or not password:
            return jsonify({"error": "Email and password are required"}), 400

        try:
            # Get database cursor
            db = get_db()

            # Check if the user exists
            db.execute("SELECT password FROM users WHERE email = %s", (email,))
            user_data = db.fetchone()

            if user_data:
                # User exists, check the password
                stored_password = user_data['password']
                if password == stored_password:
                    return jsonify({"message": "Login successful"})
                else:
                    return jsonify({"error": "Invalid password"}), 401
            else:
                return jsonify({"error": "User not found"}), 404

        except Exception as e:
            print(f"Error: {e}")
            return jsonify({"error": "Database error"}), 500

def register():
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
        if user_exists(name):
            return jsonify({"error": "User already exists"}), 409

        # Insert the new user into the database
        db.execute("INSERT INTO users (name, password, email) VALUES (%s, %s, %s)", (name, password, email))
        current_app.config['DB_CONNECTION'].commit()

        return jsonify({"message": "User successfully registered"})

    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"error": "Database error"}), 500

# Register close_db to be called after each request
current_app.teardown_appcontext(close_db)