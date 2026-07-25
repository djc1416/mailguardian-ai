from modules.ai_client import ask_ai

def summarize_email(email):
    prompt = f"""
You are an email summarization assistant.

Summarize the email below.

Rules:
- Return only the summary. 
- Maximun 3 bullet points.
- Keep the most important information.
- Do not add information that is not in the email.

Email:
{email}
"""
    return ask_ai(prompt)