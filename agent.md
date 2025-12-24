This is the documentation of my implementation journey about agents in AI.

Chronological documentation to develop and learn the agent by starting simple, then gradually increasing the complexity.

- Step 1: Simple CLI-based AI chat that answers, nothing more.
- Step 2: Adding Simple Memory with list.
- Step 3: Adding tool/s, probably Weather, Calculator, News, Arxiv, Wikipidea, etc.
- Step 4: Creating Endpoint using FastAPI.
- Step 5: Adding GUI using Streamlit or Gradio or just vibecoded site.
- Step 6: Adding the RAG for pdfs using Vector store.
- Step 7: Adding multiple agents, proly a Research Agent
- Step 8: Adding MCP server.

# Journey

## Step 1 : Simple CLI-based AI chat that answers, nothing more.
Date: 24th December, 2025
Modules used: langchain, dotenv, langchain-google-genai
<details>
<summary>Click to View the Code</summary>
    
    from langchain_google_genai import ChatGoogleGenerativeAI
    from langchain.agents import create_agent
    from dotenv import load_dotenv

    load_dotenv()

    def user():
        intent = input("User Query: ")
        return intent

    def initialize(llm=(ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature = 0.7))):

        agent = create_agent(
            model=llm,
            system_prompt="you are a helpful, but only answers in long when necessary."
        )
        return agent


    def main():
        response = initialize().invoke(
            {
                "messages": [
                    {"role": "user",
                    "content": user()}
                ]
            }
        )

        return response["messages"][-1].pretty_print()

    if __name__ == "__main__":
    while True:
        print(main())

        if user() == "exit":
            break
    
</details>
<br>

> But I don't know why I had to type the user intent 2 times for the answer.