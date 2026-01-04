from langchain_groq import ChatGroq
from langchain.agents import create_agent
from weather import get_weather_info
from arxiv_retriever import arxiv_search
from langchain.tools import tool
from dotenv import load_dotenv

load_dotenv()

def intent():
    query = input("what do you want to know? ")
    return query


@tool("weather")
def weather_tool(query):
    '''
    Searches weather for the specified city.
    '''
    res = get_weather_info(name=query)
    return res

@tool("arxiv_paper_search")
def arxiv_papers(query):
    '''
    This tool searches the arxiv papers from user intent, only give the fetched papers, and a short 2 line description. NO other information.
    '''
    res = arxiv_search(query)
    return res

def llm():
    model = ChatGroq(
        model="openai/gpt-oss-120b",
        temperature=0.2
    )

    agent = create_agent(
            model=model,
            system_prompt="you are a helpful, but only answers in long when necessary.",
            tools=[weather_tool, arxiv_papers]
        )
    return agent

def result():
    res = llm().invoke(
        {
                "messages": [
                    {"role": "user",
                    "content": intent()}
                ]
            }
    )
    return res["messages"][-1].content