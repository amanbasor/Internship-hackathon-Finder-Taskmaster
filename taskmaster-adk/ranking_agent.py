import os
from google import genai
from dotenv import load_dotenv

load_dotenv()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def run_ranker(filtered_data: str) -> str:
    response = client.models.generate_content(
        model="gemini-3.5-flash-lite",
        contents=f"You are Taskmaster. Format the final opportunities cleanly with bold deadlines and bullet points.\n\nRank and format this filtered list:\n{filtered_data}"
    )
    return response.text