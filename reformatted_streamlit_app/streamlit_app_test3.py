import streamlit as st
import sqlite3
import openai
from pages import home, login, register, profile, faq, aboutus

custom_css = """
<style>
/* Your custom CSS styles here */
*::before li,
*::after li{
    display: none !important;
}
div.st-emotion-cache-1oe5cao.eczjsme9[data-testid="stSidebarNavItems"] {
    display: none !important;
</style>
"""

st.markdown(custom_css, unsafe_allow_html=True)

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

# Main function to run the Streamlit app
def main():
    create_table()  # Ensure the users table is created when the app starts

    st.sidebar.title("MindEase")
    page = st.sidebar.radio("", ["Home", "Login", "Register", "Profile", "About Us", "FAQ"])

    if page == "Home":
        home.home_page()
    elif page == "Login":
        login.login_page()
    elif page == "Register":
        register.register_page()
    elif page == "FAQ":
        faq.faq_page()
    elif page == "About Us":
        aboutus.aboutus_page()
    elif page == "Profile":
        if "logged_in" not in st.session_state or not st.session_state.logged_in:
            st.write("Please login to access this page.")
        else:
            profile.profile_page()

if __name__ == "__main__":
    main()
