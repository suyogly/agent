from fastapi import FastAPI, Body
from fastapi.responses import StreamingResponse
from langchain_groq import ChatGroq
from langchain.agents import create_agent
from weather import get_weather_info
from arxiv_retriever import arxiv_search
from langchain.tools import tool
from dotenv import load_dotenv

load_dotenv()

# --- Tools and Setup ---
@tool("weather")
def weather_tool(query):
    '''Searches weather for the specified city.'''
    return get_weather_info(name=query)

@tool("arxiv_paper_search")
def arxiv_papers(query):
    '''Searches arxiv papers; gives fetched papers and a 2-line description.'''
    return arxiv_search(query)

# Initialize the agent globally once
model = ChatGroq(model="openai/gpt-oss-120b", temperature=0.2, streaming=True)
agent = create_agent(
    model=model,
    system_prompt="you are a helpful, but only answers in long when necessary.",
    tools=[weather_tool, arxiv_papers]
)

# --- FastAPI Configuration ---
app = FastAPI(title="LangChain Agent API")

@app.post("/ask")
async def ask_agent(payload: dict = Body(...)):
    """
    Takes a JSON body like: {"query": "What is the weather in London?"}
    """
    # 1. Extract the input (without Pydantic validation)
    user_query = payload.get("query", "Hello")
    
    async def event_stream():
        async for chunk in agent.astream_events({
            "messages": [
                {"role": "user", "content": user_query}
            ]
        }):
            yield str(chunk) + "\n"
            print(chunk)  # Log to console for debugging
    
    return StreamingResponse(event_stream(), media_type="text/plain")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
