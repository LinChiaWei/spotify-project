import psycopg2
from models.get_data import get_data
from models.update_db import update_data

def check_db():
    connection = psycopg2.connect(database="postgres",user="postgres",password="postgres",host="127.0.0.1",port='5432')
    
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM song_list;")
    connection.close()

    return bool(cursor.rowcount)


