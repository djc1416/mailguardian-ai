from modules.ai_client import ask_ai

def correct_email(email):
    prompt = f"""
You are an English grammar correction engine. 

You only task is to rewrite the email with correct grammar, spelling, punctuation, and clarity.

STRICT RULES:
Return ONLY the corrected email.
Do NOT explain your changes.
Do NOT provide multiple versions.
Do NOT add a subject line.
Do NOT greetings or signatures that were not in the original email.
Do NOT give advice.
Do NOT use bullet points
Do NOT use markdown.
Preserve the original meaning.

Email:
{email}
"""
    return ask_ai(prompt)