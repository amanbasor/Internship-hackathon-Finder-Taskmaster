import time
from research_agent import run_researcher
from eligibility_agent import run_eligibility
from ranking_agent import run_ranker

def run_opportunity_workflow(query: str) -> str:
    # 1. Scrape/Research
    raw_data = run_researcher(query)
    time.sleep(2)  # Pause to respect free tier rate limits
    
    # 2. Filter Eligibility
    filtered_data = run_eligibility(raw_data)
    time.sleep(2)  # Pause to respect free tier rate limits
    
    # 3. Format & Rank
    final_output = run_ranker(filtered_data)
    
    return final_output