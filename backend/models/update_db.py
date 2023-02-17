import psycopg2
from models.update_data import update_data

def update_db(new_data):
    exists = False
    # try:
    connection = psycopg2.connect(database="postgres",user="postgres",password="postgres",host="db",port='5432')

    cursor = connection.cursor()

    # cursor.execute("SELECT * FROM song_list;")
    # connection.commit()
    # connection.close()
    # print("select Table successfully")
    # bool(cursor.rowcount)
    # print(exists)
    # if(bool(cursor.rowcount)):
    #     data = get_data()
    #     print("Table doesn't exist")
    #     cursor.executemany("INSERT INTO song_list (song_name, image_url, song_count) VALUES(%s, %s, %s)", data)
    #     print("Create Table successfully")
    #     connection.commit()
    #     connection.close()
    # else:

    cursor.execute("SELECT * FROM song_list;")
    print("select Table successfully")
    db_data = cursor.fetchall()
    updated_data = update_data(db_data,new_data)
    print("update data sucessfully")
    cursor.execute("TRUNCATE TABLE song_list;")
    print("clear table sucessfully")
    cursor.executemany("INSERT INTO song_list (song_name, image_url, song_count) VALUES(%s, %s, %s)", updated_data)
    print("insert table sucessfully")
    connection.commit()
    connection.close()



    # connection.commit()
    # connection.close()
        
    # except:
    #         data = get_data()
    #         print("Table doesn't exist")
    #         cursor.executemany("INSERT INTO song_list (song_name, image_url, song_count) VALUES(%s, %s, %s)", data)
    #         print("Insert Table successfully")

    # except (Exception, psycopg2.Error) as error:
    #     print("Failed to insert record into table,", error)

    # finally:
    #     # closing database connection.
    #     if connection:
    #         cursor.close()
    #         connection.close()
    #         print("PostgreSQL connection is closed")