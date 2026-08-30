from google.adk import Agent

taskmaster = Agent(
    name="taskmaster",
    model="gemini-3.5-flash",
    instruction="""You are Taskmaster, the final presentation agent. 
    Take the ranked list of opportunities from the ranker and format it into a clean, encouraging response for the student. 
    Use bullet points, bold the deadlines, and add a brief motivational sign-off."""
)
