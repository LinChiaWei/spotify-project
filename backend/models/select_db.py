import psycopg2
from models.get_data import get_data
from models.update_db import update_data

def update_db():
    exists = False
    try:
        connection = psycopg2.connect(database="postgres",user="postgres",password="postgres",host="db",port='5432')

        cursor = connection.cursor()

        # sql = """CREATE TABLE IF NOT EXISTS Song_List (
        #     song_name TEXT NOT NULL UNIQUE,
        #     image_url TEXT NOT NULL,
        #     song_count TEXT NOT NULL,);"""

        cursor.execute("SELECT * FROM song_list")
        print("select Table successfully")
        exists = cursor.fetchone()[0]
        print(exists)
        if(exists):
            data = get_data()
            print("Table doesn't exist")
            cursor.executemany("INSERT INTO song_list (song_name, image_url, song_count) VALUES(%s, %s, %s)", data)
            print("Insert Table successfully")
        else:
            db_data = cursor.fetchall()
            new_data = get_data()
            print(db_data)
            # update_data(db_data,new_data)
            print("update data sucessfully")
            # cursor.execute("truncate song_list")
            print("clear table sucessfully")
            # cursor.executemany("INSERT INTO song_list (song_name, image_url, song_count) VALUES(%s, %s, %s)", db_data)
            # print("insert table sucessfully")


        connection.commit()
        connection.close()
  
    except (Exception, psycopg2.Error) as error:
        print("Failed to insert record into table,", error)

    finally:
        # closing database connection.
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")