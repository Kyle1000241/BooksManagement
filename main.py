from fastapi import FastAPI
from routers import authors, api_key, books
from database import create_database

app = FastAPI(
    title="Book Management System",
    description="An API for managing books authors and genres",
    version="1.0.0"
)

app.include_router(authors.router, prefix='/api/authors', tags=["Authors"])
app.include_router(books.router, prefix='/api/books', tags=["Books"])
app.include_router(api_key.router, prefix='/api/validate_key')

@app.on_event('startup')
def startup():
    create_database()
