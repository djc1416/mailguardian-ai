from modules.grammar import correct_email
from modules.tone import improve_tone   
from modules.subject import generate_subject
from modules.phishing import detect_phishing
from modules.summary import summarize_email
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
tone= st.selectbox(
    "Select a tone",
    [
        "Professional",
        "Friendly",
        "Formal",
        "Casual",
    ]
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

        st.subheader("Tone Improvement")
        improved_email = improve_tone(email, tone)
        st.code(improved_email)
        
        st.subheader("Suggested Subject")
        generated_subject = generate_subject(email)
        st.code(generated_subject)
       
        st.subheader("Phishing Detection")
        phising_result = detect_phishing(email)
        st.code(phising_result)

        st.subheader("Email Summary")
        summary = summarize_email(email)
        st.code(summary)