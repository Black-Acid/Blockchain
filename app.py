import redis
from fastapi import FastAPI
import schema as sma

app = FastAPI()

# redis_client = redis.Redis(host='localhost', port=6379, db=0)


redis_client = redis.Redis(
    host="redis-13945.c309.us-east-2-1.ec2.redns.redis-cloud.com",
    port=13945,
    password="gGrfy1kXiT2W6GvM7FICbTD4dYOqbEcT",
    decode_responses=True
)

books = {
    "Good-Samaritan": {
        "author": "James Brown",
        "rating": 5,
    },
    "Python":{
        "author": "BlackAcid",
        "rating": 4
    }
}

@app.get("/api/get-all-books")
def get_available_books():
    return books



@app.post("/api/add-a-book")
def add_new_book(post_request: sma.BooksPostRequest):
    if post_request.title in books:
        return f"{post_request.title} already exists"
    
    books[post_request.title] = {
        "author": post_request.author,
        "rating": post_request.rating
    }
    
    return "Your Book has been successfully added"

@app.put("/api/update-a-book")
def updateBook(post_request: sma.BooksPostRequest):
    if post_request.title in books:
        books[post_request.title] = {
            "author": post_request.author,
            "rating": post_request.rating
        }
        return books[post_request.title]
    return f"{post_request.title} does not exist"
    