from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="Book API")


class Book(BaseModel):
    title: str
    author: str
    year: int


books = [
    {"id": 1, "title": "Clean Code", "author": "Robert C. Martin", "year": 2008},
    {"id": 2, "title": "Fluent Python", "author": "Luciano Ramalho", "year": 2015},
]


@app.get("/books")
def get_books():
    return books


@app.post("/books")
def create_book(book: Book):
    # TODO: Add validation, assign an ID, and append the new book.
    return {"message": "Book created"}


@app.get("/books/{book_id}")
def get_book(book_id: int):
    # TODO: Find the book by ID and return it or raise a 404 error.
    return {"message": f"Book {book_id} details"}


@app.put("/books/{book_id}")
def update_book(book_id: int, book: Book):
    # TODO: Update the book data and return the updated record.
    return {"message": f"Book {book_id} updated"}


@app.delete("/books/{book_id}")
def delete_book(book_id: int):
    # TODO: Remove the book by ID and return a success message.
    return {"message": f"Book {book_id} deleted"}
