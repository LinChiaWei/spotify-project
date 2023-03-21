from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from models.get_data import get_data, count_song
from models.insert_db import insert_db
from models.check_db import check_db
from models.get_db_data import get_db_data
from models.update_data import check_duplicate


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
    # print(new_data)
    
    if(check):
        old_data = get_db_data()
        # print(old_data)
        data_in = check_duplicate(old_data,new_data)
        print(data_in)
        insert_db(data_in)
    else:
        insert_db(new_data)

    data = get_db_data()
    count_data = count_song(data)
    # print(count_data)
    return {"message": count_data}

# @app.get("/callback")
# def backend():
#     print("HELLO")
    