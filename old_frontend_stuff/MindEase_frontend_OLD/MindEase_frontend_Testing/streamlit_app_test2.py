import streamlit as st
import sqlite3
import openai

# Set up OpenAI API key
openai.api_key = "your_openai_api_key"

def create_table():
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL UNIQUE,
                password TEXT NOT NULL,
                email TEXT NOT NULL UNIQUE
                )''')
    conn.commit()
    conn.close()

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

# Function to logout the user
def logout():
    st.session_state.logged_in = False
    st.session_state.username = None
    st.info("You have been logged out.")

# Function to display the home page
def home():
    st.title("Home Page")
    st.write("Welcome to the home page.")
    # st.write("You are logged in as:", st.session_state.username)
    st.title("Chat with MindEase Companion")
    user_input = st.text_input("You:", "")
    if user_input:
        response = openai.Completion.create(
            engine="text-davinci-003",  # You can change the model to suit your preference
            prompt=f"User: {user_input}\nBot:"
        )
        st.text_area("Bot:", value=response.choices[0].text.strip(), height=200)
    st.button("Logout", on_click=logout)

# Function to display the login page with LLM chatbot
def login_page():
    st.title("Login")
    username_or_email = st.text_input("Username/Email")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        login(username_or_email, password)

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

# Function to display the profile page with LLM chatbot
def profile():
    st.title("Profile")
    st.write("Username:", st.session_state.username)
    st.button("Logout", on_click=logout)
    # Add the LLM chatbot to the profile page
    st.title("Chat with MindEase Companion")
    user_input = st.text_input("You:", "")
    if user_input:
        response = openai.Completion.create(
            engine="text-davinci-003",  # You can change the model to suit your preference
            prompt=f"User: {user_input}\nBot:"
        )
        st.text_area("Bot:", value=response.choices[0].text.strip(), height=200)

# Main function to run the Streamlit app
def main():
    create_table()  # Ensure the users table is created when the app starts

    st.sidebar.title("MindEase")
    page = st.sidebar.radio("", ["Home", "Login", "Register", "Profile"])

    if page == "Home":
        home()
    elif page == "Login":
        login_page()
    elif page == "Register":
        register_page()
    elif page == "Profile":
        if "logged_in" not in st.session_state or not st.session_state.logged_in:
            st.write("Please login to access this page.")
        else:
            profile()
            
if __name__ == "__main__":
    main()
