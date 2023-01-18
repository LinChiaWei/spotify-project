import psycopg2

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
