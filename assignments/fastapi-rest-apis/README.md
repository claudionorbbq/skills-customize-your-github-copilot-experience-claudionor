# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn how to build a simple REST API using FastAPI, including route definitions, request validation, and response handling for a small application.

## 📝 Tasks

### 🛠️ Create a Book API

#### Descrição
Build a small API that manages a collection of books. The application should expose endpoints for listing and creating records.

#### Requisitos
O programa concluído deve:

- Create a FastAPI application instance.
- Define a `GET /books` endpoint that returns the current list of books.
- Define a `POST /books` endpoint that accepts a JSON payload.
- Use a Pydantic model to validate the incoming request body.
- Return a proper JSON response with the created book.

### 🛠️ Add CRUD Functionality

#### Descrição
Extend the API so it supports viewing, updating, and deleting individual books by ID.

#### Requisitos
O programa concluído deve:

- Define a `GET /books/{book_id}` endpoint.
- Define a `PUT /books/{book_id}` endpoint to update an existing book.
- Define a `DELETE /books/{book_id}` endpoint to remove a book.
- Return a `404` response when a book is not found.
- Keep the data in memory with a Python list or dictionary while the server is running.

### 🛠️ Document and Test the API

#### Descrição
Prepare the API so it is easy to use and verify through the automatic FastAPI documentation and a few tests.

#### Requisitos
O programa concluído deve:

- Use FastAPI's built-in Swagger UI and ReDoc documentation.
- Add descriptive response models or examples to improve clarity.
- Write at least two tests covering successful and missing-resource behavior.
- Run the app locally and confirm the endpoints work as expected.
