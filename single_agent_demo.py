import os
from dotenv import load_dotenv
from crewai import Agent, Task, Crew
from crewai_tools import SerperDevTool
from langchain_openai import ChatOpenAI

load_dotenv()

SERPER_API_KEY = os.getenv("SERPER_API_LEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_LEY")

search_tool = SerperDevTool()


def create_research_agent():
    return Agent(
        role = "Reasearch_Agent"
        
        
        
        
        
        
    )
