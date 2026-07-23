from modules.grammar import correct_email

import streamlit as st

st.set_page_config(
    page_title="MailGuardian IA",
    layout="centered",

)   

st.title("MailGuardian IA")

st.write("AI-powered email assistant that helps users improve emails and detect phishing attempts.")

email= st.text_area(
    "Paste your email below:",
    height=250,
    placeholder="Paste your email here..."  
)

if st.button("Analyze Email"):
    if email.strip() == "":
        st.warning("Please paste an email to analyze.")
    else:
        st.success("Analyzing your email...")

        st.header("Email Analysis Results")

        st.subheader("Grammar Correction")
        corrected_email = correct_email(email)
        st.code(corrected_email)

        st.subheader("Tone Analysis")
        st.info("Comming soon: The AI will analyze the tone of your email and provide feedback.")

        st.subheader("Suggested Subject")
        st.info("Comming soon: The AI will suggest a subject line for your email.")   

        st.subheader("Phishing Detection")
        st.info("Comming soon: The AI will analyze your email for potential phishing attempts and provide a risk assessment.")

        st.subheader("Summary")
        st.info("Comming soon: The AI will provide a summary of your email content.")