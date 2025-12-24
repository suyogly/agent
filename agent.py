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

