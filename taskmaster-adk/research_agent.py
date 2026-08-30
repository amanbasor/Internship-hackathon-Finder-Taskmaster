import os
from google import genai
from dotenv import load_dotenv

load_dotenv()
# Use GEMINI_API_KEY environment variable or pass string directly as api_key="..."
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def run_researcher(query: str) -> str:
    response = client.models.generate_content(
        model="gemini-3.5-flash-lite",
        contents=f"You are a research agent. Find current student internships, hackathons, and scholarship opportunities for: {query}"
    )
    return response.text