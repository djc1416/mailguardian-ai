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

- Then write:
Reasons:
- ...

- Then write:
Suspicious phrases:
- List the suspicious phrases exactly as they appear in the email.
- If none exist, write "None".

- Finally write:
Recommendation:
- ...

Return only the analysis.

Email:
{email}
"""
    return ask_ai(prompt)