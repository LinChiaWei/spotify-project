import psycopg2
from models.get_data import get_data
from models.update_db import update_data

def check_db():
    try:
        connection = psycopg2.connect(
            database="postgres",
            user="postgres",
            password="postgres",
            host="127.0.0.1",
            port='5432'
        )
        print("Database opened successfully")

        cursor = connection.cursor()

        cursor.execute("""
            SELECT EXISTS (
                SELECT 1
                FROM information_schema.tables
                WHERE table_name = 'listened_list'
            );
        """)

        table_exists = cursor.fetchone()[0]

        if table_exists:
            print("Table 'listened_list' already exists.")
        else:
            print("Table 'listened_list' does not exist. Creating...")

            cursor.execute("""
                CREATE TABLE IF NOT EXISTS listened_list (
                    song_id SERIAL PRIMARY KEY,
                    song_name TEXT NOT NULL,
                    artist TEXT NOT NULL,
                    image_url TEXT NOT NULL,
                    timestamp_column TIMESTAMP NOT NULL
                );
                CREATE TABLE IF NOT EXISTS genres (
                    genre_id SERIAL PRIMARY KEY,
                    genre TEXT NOT NULL
                );
                CREATE TABLE IF NOT EXISTS song_genre (
                    song_id INT,
                    genre_id INT,
                    FOREIGN KEY (song_id) REFERENCES listened_list(song_id),
                    FOREIGN KEY (genre_id) REFERENCES genres(genre_id)
                );
            """)
            print("Table 'listened_list' created successfully.")

        cursor.close()
        connection.close()
        return table_exists

    except psycopg2.Error as e:
        print("Error connecting to the database:", e)


