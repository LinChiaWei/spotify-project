import psycopg2

def insert_db(data):
    try:
        connection = psycopg2.connect(database="postgres",user="postgres",password="postgres",host="127.0.0.1",port='5432')

        cursor = connection.cursor()
        for i in data:
            song_detail = i[:4]
            genre_data = i[4]
            cursor.execute("INSERT INTO listened_list (song_name, artist, image_url, timestamp_column) VALUES(%s, %s, %s, %s) RETURNING song_id", song_detail)
            song_id = cursor.fetchone()[0]
            # print(cursor.fetchone()[0])
            # print(song_id)
            for genre in genre_data:
                cursor.execute("SELECT genre_id FROM genres WHERE genre = %s", (genre,))
                existing_genre = cursor.fetchone()
                if existing_genre:
                    genre_id = existing_genre[0]
                else:
                    cursor.execute("INSERT INTO genres (genre) VALUES (%s) RETURNING genre_id", (genre,))
                    genre_id = cursor.fetchone()[0]

                cursor.execute("INSERT INTO song_genre (song_id, genre_id) VALUES (%s, %s)", (song_id, genre_id))

        print("Insert Table successfully")
        
        connection.commit()
        connection.close()
  
    except (Exception, psycopg2.Error) as error:
        print("Failed to insert record into table: ", error)

    finally:
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")