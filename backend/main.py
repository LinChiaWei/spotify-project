from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi_utils.session import FastAPISessionMaker
from fastapi_utils.tasks import repeat_every

from db_manager import DatabaseManager

from models.get_data import get_data, count_song, count_artist, get_user_info
from models.check_db import check_db
from models.update_data import check_duplicate


from datetime import datetime


app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:8080",
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
    db_manager = DatabaseManager()
    new_data = get_data()

    if(db_manager.check_db()):
        existing_data = db_manager.get_song()
        insert_data = check_duplicate(existing_data,new_data)
        print(insert_data)
        insert_db(insert_data)
    else:
        insert_db(new_data)



@app.get("/songs")
def Data_get(start_date:str=None, end_date:str=None):
    user_info = get_user_info()
    song_Data = get_db_song(start_date,end_date)
    count_data = count_song(song_Data)
    return {"message": count_data,"user_info":user_info}

@app.get("/artists")
def Data_get(start_date:str=None, end_date:str=None):
    artist_data = get_db_song(start_date,end_date)
    count_data = count_artist(artist_data)
    return {"message": count_data}

@app.get("/genres")
def Data_get(start_date:str=None, end_date:str=None):
    genres_data = get_db_song(start_date,end_date)
    count_data = count_artist(genres_data)
    return {"message": count_data}


@app.get("/history")
def Data_get(start_date:str=None, end_date:str=None):
    if start_date != None and end_date != None:
        song_Data = get_db_song(start_date,end_date)
        return {"message": song_Data}
    else:
        song_Data = get_history(num=50)
        return {"message": song_Data}

    
