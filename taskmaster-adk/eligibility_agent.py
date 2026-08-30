import os
from google import genai
from dotenv import load_dotenv

load_dotenv()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def run_eligibility(raw_data: str) -> str:
    response = client.models.generate_content(
        model="gemini-3.5-flash-lite",
        contents=f"You are an eligibility checker. Filter out anything requiring professional experience or missed deadlines. Keep undergraduate options.\n\nReview this list:\n{raw_data}"
    )
    return response.text