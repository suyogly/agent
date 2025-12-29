from langchain_groq import ChatGroq
from langchain.agents import create_agent
from langchain_tavily import TavilySearch
from weather import get_weather_info
from langchain.tools import tool
from dotenv import load_dotenv

load_dotenv()
def get_city():
    name = input("Enter the name of the city: ")
    return name

@tool("weather")
def weather_tool():
    '''
    Searches weather for the specified city.
    '''
    res = get_weather_info(name=get_city())
    return res

model = ChatGroq(
    model="openai/gpt-oss-120b",
    temperature=0.2
)

agent = create_agent(
        model=model,
        system_prompt="you are a helpful, but only answers in long when necessary.",
        tools=[weather_tool]
    )

res = agent.invoke(
    {
            "messages": [
                {"role": "user",
                "content": get_city()}
            ]
        }
)

print(res["messages"][-1].content)