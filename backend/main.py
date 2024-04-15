from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi_utils.session import FastAPISessionMaker
from fastapi_utils.tasks import repeat_every
from models.get_data import get_data, count_song, count_artist
from models.insert_db import insert_db
from models.check_db import check_db
from models.get_data import get_user_info
from models.get_db_data import get_db_song
from models.update_data import check_duplicate
from datetime import datetime


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

swagger_ui_default_parameters = {
    "dom_id": "#swagger-ui",
    "layout": "BaseLayout",
    "deepLinking": True,
    "showExtensions": True,
    "showCommonExtensions": True,
}

@app.on_event("startup")
@repeat_every(seconds=60*90)  # 1 hour
def update_data():
    check = check_db()
    new_data = get_data()
    if(check):
        old_data = get_db_song()
        data_in = check_duplicate(old_data,new_data)
        print(data_in)
        insert_db(data_in)
    else:
        insert_db(new_data)



@app.get("/songs")
def Home_get(start_date:str=None,end_date:str=None):
    user_info = get_user_info()
    song_Data = get_db_song(start_date,end_date)
    count_data = count_song(song_Data)
    # print(count_data)
    return {"message": count_data,"user_info":user_info}

@app.get("/artists")
def Home_get(start_date:str=None,end_date:str=None):
    user_info = get_user_info()
    artist_Data = get_db_song(start_date,end_date)
    count_data = count_artist(artist_Data)
    # print(count_data)
    return {"message": count_data}

@app.get("/genres")
def Home_get(start_date:str=None,end_date:str=None):
    user_info = get_user_info()
    artist_Data = get_db_song(start_date,end_date)
    count_data = count_artist(artist_Data)
    # print(count_data)
    return {"message": count_data}

@app.get("/thismonth")
def This_month_data(start_date:str=None,end_date:str=None):
    user_info = get_user_info()
    data = get_db_song(start_date,end_date,type="this")
    count_data = count_song(data)

    return {"message": count_data,"user_info":user_info}
    
@app.get("/lastmonth")
def Last_month_data(start_date:str=None,end_date:str=None):
    user_info = get_user_info()
    data = get_db_song(start_date,end_date,type="last")
    count_data = count_song(data)
    return {"message": count_data,"user_info":user_info}
    
