from langchain_groq import ChatGroq
from langchain.agents import create_agent
from langchain_tavily import TavilySearch
from dotenv import load_dotenv

load_dotenv()

intent = input("What do you want to know?")

search_tool = TavilySearch(
    max_results = 1
)

llm = ChatGroq(model="openai/gpt-oss-120b", temperature=0.7)

agent = create_agent(
    model=llm,
    system_prompt="you are the helpful assistant.",
    tools=[search_tool]
)

res = search_tool.invoke({"query": intent})
print(res['results'][0]['content'])
