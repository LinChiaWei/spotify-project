import psycopg2

def insert_db(data):
    try:
        connection = psycopg2.connect(database="postgres",user="postgres",password="postgres",host="127.0.0.1",port='5432')

        cursor = connection.cursor()


        # cursor.executemany(
        #     "INSERT INTO song_list (song_name, image_url, day_) VALUES(%s, %s, %s) \
        #         ON DUPLICATE KEY UPDATE (song_name, image_url, day_) VALUES(%s, %s, %s) ", data)
        
        # print(data)
        cursor.executemany("INSERT INTO song_list (song_name, image_url, day_) VALUES(%s, %s, %s)", data)
        # cursor.executemany("INSERT INTO song_list (song_name, image_url, day_) VALUES(%s, %s, %s)", data)
        # for record in data:
        #     print(type(record[0]), type(record[1]), type(record[2]))
        #     cursor.executemany(
        #     "INSERT INTO song_list (song_name, image_url, day_) VALUES (%s, %s, %s) WHERE NOT EXISTS (SELECT * FROM song_list WHERE day_ = %s)",
        #     (record[0], record[1], record[2], record[2])
        #     )


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