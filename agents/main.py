from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Welcome to my Book API!"}

# Our fake database (for now)
books_db = {
    1: {"id": 1, "title": "The Hobbit", "author": "J.R.R. Tolkien", "year": 1937},
    2: {"id": 2, "title": "1984", "author": "George Orwell", "year": 1949},
    3: {"id": 3, "title": "Dune", "author": "Frank Herbert", "year": 1965}
}

@app.get("/books/{book_id}")
def get_book(book_id: int):
    if book_id in books_db:
        return books_db[book_id]
    else:
        return {"error": "Book not found"}


@app.get("/authors/{author_name}/books/{book_id}")
def get_author_book(author_name: str, book_id: int):
    return {
        "author": author_name,
        "book_id": book_id,
        "message": f"Getting book {book_id} by {author_name}"
    }


@app.get("/about")
def about():
    return {"message": "This API helps you manage your book collection"}
