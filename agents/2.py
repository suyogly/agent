from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_groq import ChatGroq
from langchain.agents import create_agent
from dotenv import load_dotenv

load_dotenv()

history = [] # memory with list
def user():
    intent = input("User Query: ")
    return f"{intent} + {history}"

def initialize(llm=(ChatGroq(model="openai/gpt-oss-120b", temperature = 0.7))):

    agent = create_agent(
        model=llm,
        system_prompt="you are a helpful, but only answers in long when necessary. the user will give you the prompt like this: 'something' + [list], there the string is real input and anything inside the list is conversation history of you and the user. dont repeat history, just go with the flow using the history."
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

    res = response["messages"][-1].content
    history.append(res) # append to history
    return res


if __name__ == "__main__":
    while True:
        print(main())

