import psycopg2
from datetime import datetime

def get_db_song(start_date=None,end_date=None,type=None):
    connection = psycopg2.connect(database="postgres",user="postgres",password="postgres",host="127.0.0.1",port='5432')
    cursor = connection.cursor()
    result = []
    if start_date != None and end_date != None:
        cursor.execute("SELECT ll.song_name, a.artist_name, a.img_url, ll.image_url, ll.timestamp_column\
                        FROM listened_list ll \
                        INNER JOIN artist a ON ll.artist_id = a.artist_id \
                        WHERE ll.timestamp_column BETWEEN %s AND %s;", (start_date, end_date))
    else:
        cursor.execute("SELECT ll.song_name, a.artist_name, a.img_url, ll.image_url, timestamp_column \
                        FROM listened_list ll \
                        INNER JOIN artist a ON ll.artist_id = a.artist_id;")
                        
    rows = cursor.fetchall()
    connection.close()
    
    return rows

def get_history(num = 50):
    connection = psycopg2.connect(database="postgres",user="postgres",password="postgres",host="127.0.0.1",port='5432')
    cursor = connection.cursor()
    result = []
    cursor.execute("SELECT ll.song_name, a.artist_name, a.img_url, ll.image_url, ll.timestamp_column\
                    FROM listened_list ll \
                    INNER JOIN artist a ON ll.artist_id = a.artist_id \
                    ORDER BY ll.timestamp_column DESC LIMIT %s;", (num,))
 
    rows = cursor.fetchall()

    connection.close()
    
    return rows


def get_genres_db():
    connection = psycopg2.connect(database="postgres",user="postgres",password="postgres",host="127.0.0.1",port='5432')
    cursor = connection.cursor()
    cursor.execute("SELECT song_id, genres_id FROM song_genres;")
    rows = cursor.fetchall()

    result = []
    for(row) in rows:
        corsor.execute("SELECT song_name FROM listened_list WHERE id = %s;",(row[0],))
        song = cursor.fetchone()
        corsor.execute("SELECT genres FROM genres WHERE id = %s;",(row[1],))
        genre = cursor.fetchone()
        result.append((row[0],genre[0]))