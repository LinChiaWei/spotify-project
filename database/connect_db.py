import psycopg2

connection = psycopg2.connect(database="postgres",user="postgres",password="postgres",host="127.0.0.1",port='5432')

cursor = connection.cursor()

sql = """CREATE TABLE SongInf (
    SongName TEXT NOT NULL,
    AuthorName TEXT NOT NULL,
    """

cursor.execute(sql)
print("Table created successfully")

connection.commit()
connection.close()
