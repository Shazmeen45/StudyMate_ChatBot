import os
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY was not found in the .env file.")

client = genai.Client(api_key=api_key)


system_prompt = """
You are StudyMate, a helpful study assistant.

Your job is to help students understand study topics
in simple and clear language.

Follow these rules:

- Explain difficult topics in simple words.
- Give examples when they help.
- Keep answers organized and easy to read.
- Use the previous conversation when answering follow-up questions.
- Do not make answers unnecessarily complicated.
- If you are not sure about something, say that clearly.
"""


def create_chat():
    chat = client.chats.create(
        model="gemini-3.5-flash-lite",
        config=types.GenerateContentConfig(
            system_instruction=system_prompt
        )
    )

    return chat


def get_response(chat, user_message):
    response = chat.send_message(user_message)
    return response.text