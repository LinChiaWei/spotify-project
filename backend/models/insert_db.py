import psycopg2

def insert_db(data):
    try:
        connection = psycopg2.connect(database="postgres",user="postgres",password="postgres",host="127.0.0.1",port='5432')

        cursor = connection.cursor()
        cursor.executemany("INSERT INTO song_list (song_name, artist, image_url, timestamp_column) VALUES(%s, %s, %s, %s)", data)
 
        print("Insert Table successfully")
        
        connection.commit()
        connection.close()
  
    except (Exception, psycopg2.Error) as error:
        print("Failed to insert record into mobile table", error)

    finally:
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")