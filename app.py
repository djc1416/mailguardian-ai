from modules.grammar import correct_email
from modules.tone import improve_tone   
from modules.subject import generate_subject
from modules.phishing import detect_phishing
from modules.summary import summarize_email
from utils.text_utils import clean_email, is_empty
import streamlit as st

st.set_page_config(
    page_title="MailGuardian AI",
    layout="centered",

)   

st.image("assets/logo.png", width=180)

st.title("MailGuardian AI")

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
    if is_empty(email):
        st.warning("Please paste an email to analyze.")
    else:
        with st.spinner("Analyzing your email..."):
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
            if "HIGH" in phising_result.upper():
                st.error(phising_result)
            elif "MEDIUM" in phising_result.upper():
                st.warning(phising_result)
            elif "LOW" in phising_result.upper():
                st.success(phising_result)
            else:
                st.info(phising_result)       
                
            st.subheader("Email Summary")
            summary = summarize_email(email)
            st.code(summary)