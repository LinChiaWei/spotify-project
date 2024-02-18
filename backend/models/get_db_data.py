import psycopg2
from datetime import datetime

def get_db_data(start_date=None,end_date=None):
    connection = psycopg2.connect(database="postgres",user="postgres",password="postgres",host="127.0.0.1",port='5432')
    cursor = connection.cursor()

    if start_date != None and end_date != None:
        cursor.execute("SELECT (song_name, artist, image_url, timestamp_column) FROM listened_list WHERE timestamp_column BETWEEN %s AND %s;",(start_date,end_date))
    else:
        cursor.execute("SELECT song_name, artist, image_url, timestamp_column FROM listened_list;")


    rows = cursor.fetchall()
    connection.close()
    
    return rows

def get_db_month_data(start_date=None,end_date=None):
        
    connection = psycopg2.connect(database="postgres",user="postgres",password="postgres",host="127.0.0.1",port='5432')
    cursor = connection.cursor()

    if start_date != None and end_date != None:
        cursor.execute("SELECT * FROM listened_list WHERE timestamp_column BETWEEN %s AND %s;",(start_date,end_date))
    else:
        cursor.execute("SELECT * FROM listened_list WHERE timestamp_column >= date_trunc('month', CURRENT_DATE);")    
    
    rows = cursor.fetchall()
    connection.close()

    return rows