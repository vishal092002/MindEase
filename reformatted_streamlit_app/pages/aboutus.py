import streamlit as st
from pages import logout

# Function to display the home page
def aboutus_page():
    st.title("About Us Page")

    # Section: About Us
    st.header("About Us")
    st.markdown("""
    Welcome to Mindease, an innovative AI therapy company dedicated to supporting mental wellness and guiding individuals on their journey to emotional well-being. 
    At Mindease, we believe that everyone deserves access to effective and personalized mental health support, anytime and anywhere. 
    Our AI software therapy company is designed to provide transformative experiences through cutting-edge technology and compassionate guidance.
    """)

    # Section: What We Do
    st.header("What We Do")
    st.markdown("""
    Mindease specializes in developing AI-powered therapy software that combines the power of artificial intelligence with evidence-based therapeutic techniques. 
    Our software offers a range of mental health resources, tools, and guidance to help individuals navigate their emotional challenges, promote self-care, and foster personal growth. 
    Our AI therapy solutions are designed to complement traditional therapy, providing additional support and guidance to individuals seeking mental wellness.
    """)

    # Section: Our Approach
    st.header("Our Approach")
    st.markdown("""
    At Mindease, we prioritize the needs and well-being of our users. Our AI software therapy is built on a foundation of empathy, compassion, and respect for individual experiences. 
    We understand that mental health journeys are unique, and our goal is to provide personalized support that meets the diverse needs of our users.
    Our AI algorithms are continually learning and adapting, allowing us to provide tailored recommendations and guidance that align with each individual's goals and preferences. 
    Through our software, users can access a variety of therapeutic techniques, such as cognitive-behavioral therapy, mindfulness practices, and positive psychology interventions, to address their specific challenges and promote lasting change.
    """)

    # Section: Our Main Goal
    st.header("Our Main Goal")
    st.markdown("""
    The main goal of Mindease's AI software therapy company is to make mental health support accessible, effective, and inclusive. 
    We strive to break down barriers to mental health care by providing a user-friendly platform that can be accessed anytime, anywhere. 
    Our goal is to empower individuals to take control of their mental well-being and navigate life's challenges with resilience, self-compassion, and personal growth. 
    We aim to revolutionize the mental health landscape by leveraging the power of AI to deliver personalized guidance, evidence-based interventions, and a supportive community. 
    Through our AI software, we want to enable individuals to build resilience, cultivate emotional well-being, and lead fulfilling lives. 
    Join us on this transformative journey as we harness the potential of AI to revolutionize mental health support. 
    At Mindease, we are committed to helping individuals thrive, one step at a time.
    """)

    st.button("Logout", on_click=logout)