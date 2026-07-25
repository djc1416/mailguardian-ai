from modules.ai_client import ask_ai

def detect_phishing(email):
    prompt = f""" 
You are a cybersecurity assistant.

Analyze the following email for phishing indicators. 

Rules:
- Start with one risk level:
LOW
MEDIUM
HIGH
- Then explain the reasons briefly. 
- Finish with one recommendation. 
- Return only the analysis. 

Email:
{email}
"""
    return ask_ai(prompt)