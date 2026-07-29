#MailGuardian AI Architecture

## Overview

MailGuardian AI is an AI powered email assistant

The applicaton helps user improve emails by provding:

- Grammar correction
- Tone improvement
- Subject generation
- Phishing detection
- Email summary

---

## Architecture

```
User
   │
   ▼
Streamlit Interface (app.py)
   │
   ▼
Modules
   ├── grammar.py
   ├── tone.py
   ├── subject.py
   ├── phishing.py
   └── summary.py
   │
   ▼
ai_client.py
   │
   ▼
OpenRouter API
   │
   ▼
Large Language Model
```

---

## Project Structure

```
mailguardian-ai/

│

├── assets/

├── docs/

├── modules/

├── tests/

├── utils/

├── app.py

├── README.md

└── requirements.txt
```

