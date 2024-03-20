import streamlit as st
import openai
from pages import logout

# Function to display the home page
def home_page():
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