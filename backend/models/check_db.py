import psycopg2
from models.get_data import get_data
from models.update_db import update_data

def check_db():
    exists = False
    # try:
    connection = psycopg2.connect(database="postgres",user="postgres",password="postgres",host="db",port='5432')

    cursor = connection.cursor()
    # 寫入資料庫
    cursor.execute("SELECT * FROM song_list;")
    connection.close()

    return bool(cursor.rowcount)


