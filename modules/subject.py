from modules.ai_client import ask_ai

def generate_subject(email):
    prompt = f"""
You are an email assistant. 

Generate a short and professional email subject. 

Rules:
- Return only the subject. 
- Maximun 10 words. 
- Do not use quotation marks.
- Do not explain anything.

Email:  
{email}
"""
    return ask_ai(prompt)