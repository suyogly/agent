import tiktoken
from fastapi import FastAPI, Body

app = FastAPI()

@app.post("/")
def get_tokens(payload: dict = Body(...)):
    encoding = tiktoken.get_encoding("cl100k_base")

    text = payload.get("input", "")

    tokens = encoding.encode(text)
    return {"text" : text,
            "tokens" : tokens,
            "number of tokens" : len(tokens)}
    

if __name__ == "__main__":
    get_tokens()
