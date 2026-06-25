import os
from groq import Groq
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize Groq client
client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

# Model to use
MODEL_NAME = "llama-3.3-70b-versatile"


def generate_response(user_prompt: str) -> str:
    """
    Sends the user's prompt to Groq LLM and returns the AI response.

    Args:
        user_prompt (str): User's transcribed speech.

    Returns:
        str: AI-generated response.
    """

    if not user_prompt:
        return "I didn't receive any input."

    try:
        completion = client.chat.completions.create(
            model=MODEL_NAME,
            temperature=0.7,
            max_tokens=512,
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are Pathixo, a friendly, intelligent, and helpful "
                        "AI voice assistant. Respond naturally, conversationally, "
                        "and keep answers concise unless the user asks for details."
                    ),
                },
                {
                    "role": "user",
                    "content": user_prompt,
                },
            ],
        )

        return completion.choices[0].message.content.strip()

    except Exception as e:
        print(f"Groq API Error: {e}")
        return "Sorry, I couldn't generate a response at the moment."