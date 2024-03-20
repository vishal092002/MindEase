import streamlit as st 
import openai
from pages import logout

# Function to display the profile page with LLM chatbot
def profile_page():
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