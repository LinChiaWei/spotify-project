import psycopg2


def get_db_data():

    connection = psycopg2.connect(database="postgres",user="postgres",password="postgres",host="127.0.0.1",port='5432')
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM song_list;")
    rows = cursor.fetchall()
    connection.close()

    return rows

def get_db_month_data():
        
    connection = psycopg2.connect(database="postgres",user="postgres",password="postgres",host="127.0.0.1",port='5432')
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM song_list WHERE day_ >= date_trunc('month', CURRENT_DATE);")
    rows = cursor.fetchall()
    connection.close()

    return rows