import psycopg2

def create_table():
    connection = psycopg2.connect(database="postgres",user="postgres",password="postgres",host="db",port='5432')

    cursor = connection.cursor()

    print("Table created successfully")

    connection.commit()
    connection.close()
