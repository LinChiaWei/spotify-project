from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi_utils.session import FastAPISessionMaker
from fastapi_utils.tasks import repeat_every
from models.get_data import get_data, count_song
from models.insert_db import insert_db
from models.check_db import check_db
from models.get_data import get_user_info
from models.get_db_data import get_db_data,get_db_month_data
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

@app.on_event("startup")
@repeat_every(seconds=60 * 60)  # 1 hour
def update_data():
    check = check_db()
    new_data = get_data()

    print(new_data)

    if(check):
        old_data = get_db_data()
        data_in = check_duplicate(old_data,new_data)
        print(data_in)
        insert_db(data_in)
    else:
        insert_db(new_data)



@app.get("/")
def get_data(start_date:str=None,end_date:str=None):
    # check = check_db()
    # new_data = get_data()
    # print(new_data)
    user_info = get_user_info()

    # new_data = []
    # if(check):
    #     old_data = get_db_data()
    #     data_in = check_duplicate(old_data,new_data)
    #     print(data_in)
    #     insert_db(data_in)
    # else:
    #     insert_db(new_data)

    data = get_db_data(start_date,end_date)
    count_data = count_song(data)
    return {"message": count_data,"user_info":user_info}

@app.get("/thismonth")
def get_this_month_data(start_date:str=None,end_date:str=None):

    data = get_db_month_data(start_date,end_date)
    count_data = count_song(data)
    user_info = get_user_info()
    print(user_info)
    return {"message": count_data,"user_info":user_info}
    

@app.get("/lastmonth")
def get_last_month_data(start_date:str=None,end_date:str=None):

    data = get_db_month_data(start_date,end_date)
    count_data = count_song(data)
    user_info = get_user_info()
    print(user_info)
    return {"message": count_data,"user_info":user_info}
    