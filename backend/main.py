from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from models.get_data import get_data
from models.insert_db import insert_db
from models.select_db import update_db


app = FastAPI()


origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def backend():
    data = get_data()
    update_db()
    # insert_db(data)
    # print(data)
    return {"message": data}

# @app.get("/callback")
# def backend():
#     print("HELLO")
    