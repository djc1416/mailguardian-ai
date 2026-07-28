def clean_email(text):
    return text.strip()

def is_empty(text):
    return clean_email(text) == ""