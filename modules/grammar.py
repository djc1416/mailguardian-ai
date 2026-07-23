from modules.ai_client import ask_ai

def correct_email(email):
    prompt = f"Correct this email:\n\n{email}"
    return ask_ai(prompt)