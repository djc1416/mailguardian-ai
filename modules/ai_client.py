import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1"
)

def ask_ai(prompt):
    response = client.chat.completions.create(
        model="deepseek/deepseek-chat-v3-0324:free",
        messages=[
            {
                "role": "system",
                "content": "You are grammar correction engine. Always follow the user's instructions exactly. Never provide explanations or multiple options unless explicity requeseted."
            },
            {
                "role": "user",
                "content": prompt
            }

        ]
    )    
    return response.choices[0].message.content