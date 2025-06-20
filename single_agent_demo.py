import os
from dotenv import load_dotenv
from crewai import Agent, Task, Crew
from crewai_tools import SerperDevTool
from langchain_openai import ChatOpenAI

load_dotenv()

SERPER_API_KEY = os.getenv("SERPER_API_LEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

search_tool = SerperDevTool()
llm = ChatOpenAI("gpt-3.5-turbo")


def create_research_agent():
    return Agent(
        role = "Reasearch_Specialist",
        gole = "conduct through research on given topic",
        backstory = "you are an experienced researcher with expertise in finding and synthesizing information from various sources",
        verbose = True,
        allow_deligation = False,
        tools = [search_tool],
        llm = llm
        
        
    )

def create_task(agent, topic):
    return Task(
        description =f"Research on the following topic and provide a comprehensive summary : {topic}", 
        agent = agent,
        expected_output = "A detailed summery of the research findings, including key insights "
                

    )
    
def run_research(topic):
    
    agent = create_research_agent()
    task = create_task(agent, topic)
    crew = Crew(agent = [agent], task = [task])
    results = crew.kickoff()
    return results

if __name__== "__main__":
    print ("welcome to the research agents ")
    topic = input("enter the research topic")
    result = run_research(topic)
    print("research results ")