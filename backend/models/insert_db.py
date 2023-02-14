import psycopg2

def insert_db(data):
    try:
        connection = psycopg2.connect(database="postgres",user="postgres",password="postgres",host="db",port='5432')

        cursor = connection.cursor()

        # sql = """CREATE TABLE IF NOT EXISTS Song_List (
        #     song_name TEXT NOT NULL UNIQUE,
        #     image_url TEXT NOT NULL,
        #     song_count TEXT NOT NULL,);"""

        cursor.executemany("INSERT INTO song_list (song_name, image_url, song_count) VALUES(%s, %s, %s)", data)
        print("Insert Table successfully")
        
        connection.commit()
        connection.close()
  
    except (Exception, psycopg2.Error) as error:
        print("Failed to insert record into mobile table", error)

    finally:
        # closing database connection.
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")