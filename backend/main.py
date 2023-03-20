from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from models.get_data import get_data, count_song
from models.insert_db import insert_db
from models.update_db import update_db
from models.check_db import check_db
from models.get_db_data import get_db_data


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
    check = check_db()
    new_data = get_data()
    # if(check):
    # update_db(new_data)
    # else:
    insert_db(new_data)
    print(new_data)
    data = get_db_data()
    count_data = count_song(data)
    # print()
    return {"message": count_data}

# @app.get("/callback")
# def backend():
#     print("HELLO")
    