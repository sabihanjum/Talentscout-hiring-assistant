# app.py

import streamlit as st
from prompts import greeting_prompt, info_prompt, generate_tech_questions_prompt
from utils import ask_gemini

st.set_page_config(page_title="TalentScout Hiring Assistant", layout="centered")

if "stage" not in st.session_state:
    st.session_state.stage = "start"
    st.session_state.candidate_info = {}

st.title("🤖 TalentScout - AI Hiring Assistant")

if st.session_state.stage == "start":
    st.markdown(greeting_prompt())
    if st.button("Start"):
        st.session_state.stage = "info"

elif st.session_state.stage == "info":
    st.markdown(info_prompt())
    with st.form("candidate_form"):
        name = st.text_input("Full Name")
        email = st.text_input("Email Address")
        phone = st.text_input("Phone Number")
        experience = st.number_input("Years of Experience", 0, 50)
        position = st.text_input("Desired Position(s)")
        location = st.text_input("Current Location")
        tech_stack = st.text_area("Tech Stack (comma-separated)")

        submitted = st.form_submit_button("Submit")
        if submitted:
            st.session_state.candidate_info = {
                "name": name,
                "email": email,
                "phone": phone,
                "experience": experience,
                "position": position,
                "location": location,
                "tech_stack": tech_stack
            }
            st.session_state.stage = "questions"

elif st.session_state.stage == "questions":
    tech_stack = st.session_state.candidate_info["tech_stack"]
    prompt = generate_tech_questions_prompt(tech_stack)
    questions = ask_gemini(prompt)
    st.subheader("🧠 Technical Questions")
    st.markdown(questions)
    if st.button("End Conversation"):
        st.session_state.stage = "end"

elif st.session_state.stage == "end":
    st.success("Thank you for your time! We'll review your responses and get back to you soon. 👋")
