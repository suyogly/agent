This is the documentation of my implementation journey about agents in AI.

Chronological documentation to develop and learn the agent by starting simple, then gradually increasing the complexity.

- Step 1: Simple CLI-based AI chat that answers, nothing more.
- Step 2: Adding Simple Memory with list.
- Step 3: Adding tool/s, probably Weather, Calculator, News, Arxiv, Wikipidea, etc.
- Step 4: Creating Endpoint using FastAPI.
- Step 5: Adding GUI using Streamlit or Gradio or just vibecoded site.
- Step 5.5: Deploying the app using Render or Fly.io or Vercel.
- Step 6: Adding the RAG for pdfs using Vector store.
- Step 7: Adding multiple agents, proly a Research Agent
- Step 8: Adding MCP server.

# Journey

## Step 1 : Simple CLI-based AI chat that answers, nothing more. (*done*)
Date: 24th December, 2025 <br>
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

> **Problem**: But I don't know why I had to type the user intent 2 times for the answer. <br>
**Fixed**: Because I was calling user() two times, once in main() and once in the while loop. Fixed it by storing the user input in a variable.


## Step 2 : Add Memory (*done*)
Date: 24th December, 2025 22:52 PM <br>
Modules used: langchain, dotenv, langchain-groq
<details>
<summary>Click to View Code</summary>

    from langchain_google_genai import ChatGoogleGenerativeAI
    from langchain_groq import ChatGroq
    from langchain.agents import create_agent
    from dotenv import load_dotenv

    load_dotenv()

    history = []
    def user():
        intent = input("User Query: ")
        return f"{intent} + {history}"

    def initialize(llm=(ChatGroq(model="openai/gpt-oss-120b", temperature = 0.7))):

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

        res = response["messages"][-1].pretty_print()
        return res

    def memory():
        history.append(main())
        print(history)
        return history

    if __name__ == "__main__":
        while True:
            print(memory())

</details>
<br>

> **Problem**: Getting "None" value while appending to the History, and getting response on List.<br>
**Solved**: pretty_print() gives the None value when passed, so I used .content, and removed memory() function to avoid responses on list. Added .append inside main().