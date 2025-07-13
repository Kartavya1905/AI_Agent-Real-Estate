import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)

def get_llm_response(user_input):
    try:
        response = client.chat.completions.create(
            model="llama3-8b-8192",
            messages=[
                {"role": "system", "content": "You are a real estate assistant."},
                {"role": "user", "content": user_input["message"]}
            ]
        )
        return {
            "response": response.choices[0].message.content,
            "metadata": {
                "model": response.model,
                "source": "Groq"
            }
        }
    except Exception as e:
        return {
            "error": str(e),
            "source": "Groq"
        }
