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

st.button("Analyze Email")