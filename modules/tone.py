from modules.ai_client import ask_ai

def improve_tone(email, tone):
    prompt = f"""  
You are an email writing assistant. 

Rewrite the email using a {tone} tone. 

Rules:
- Keep the original meaning. 
- Improve clarity. 
- Return only the rewritten email. 
- Do not explain your changes.

Email:
{email} 
"""
    return ask_ai(prompt)
