import psycopg2
from models.get_data import get_data
from models.update_db import update_data
from models.update_data import update_data

class DB_operate():
    def create_table():
        connection = psycopg2.connect(database="postgres",user="postgres",password="postgres",host="db",port='5432')

        cursor = connection.cursor()

        # sql = """CREATE TABLE IF NOT EXISTS Song_List (
        #     song_name TEXT NOT NULL UNIQUE,
        #     image_url TEXT NOT NULL,
        #     song_count TEXT NOT NULL,);"""

        # cursor.execute(sql)
        print("Table created successfully")

        connection.commit()
        connection.close()

    def check_db():
        exists = False
        # try:
        connection = psycopg2.connect(database="postgres",user="postgres",password="postgres",host="db",port='5432')

        cursor = connection.cursor()
        # 寫入資料庫
        cursor.execute("SELECT * FROM song_list;")
        connection.close()

        return bool(cursor.rowcount)

    def get_db_data():

        connection = psycopg2.connect(database="postgres",user="postgres",password="postgres",host="db",port='5432')
        cursor = connection.cursor()

        cursor.execute("SELECT * FROM song_list;")
        rows = cursor.fetchall()
        connection.close()

        return rows

    def update_db(new_data):
        connection = psycopg2.connect(database="postgres",user="postgres",password="postgres",host="db",port='5432')
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM song_list;")
        print("select Table successfully")

        db_data = cursor.fetchall()
        updated_data = update_data(db_data,new_data)
        print("update data sucessfully")

        cursor.execute("TRUNCATE TABLE song_list;")
        print("clear table sucessfully")

        cursor.executemany("INSERT INTO song_list (song_name, image_url, song_count) VALUES(%s, %s, %s)", updated_data)
        print("insert table sucessfully")

        connection.commit()
        connection.close()