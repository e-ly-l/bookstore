from fastapi import FastAPI, Body
from models.user import User
from models.author import Author
#from models.book import Book

app = FastAPI()

@app.get("/hello")
async def hello_word():
    return {"Hello Word!"}

@app.post("/user")
async def post_user(user:User):
    return {"request body": user}

@app.get("/user") #user?password=...
async def get_user_validation(password: str):
    return {"query parameter": password}

@app.get("/book/{isbn}")
async def get_book_with_isbn(isbn: str):
    return {"query changable parameter": isbn}

@app.get("/author/{id}/book")
async def get_authors_books(id: int, category: str, order: str = "asc"):
    return {"query changable parameter": order + category + str(id)}

@app.patch("/author/name")
async def patch_author_name(name: str = Body(..., embed= True)):
    return {"name in body": name}

@app.post("/user/author")
async def post_user_and_author(user: User, author: Author,
                               bookstore_name: str = Body(..., embed= True)):
    return {"user": user, "author": author, "bookstore_name": bookstore_name}


# uvicorn run:app --reload
# uvicorn run:app --reload --port 3000