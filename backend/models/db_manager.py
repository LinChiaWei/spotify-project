import psycopg2

class DatabaseManager:
    def __init__(self):
        self.db_name = "postgres"
        self.user = "postgres"
        self.password = "postgres"
        self.host = "127.0.0.1"
        self.port = "5432"

    def connect_db(self):
        try:
            connection = psycopg2.connect(
                database=self.db_name,
                user=self.user,
                password=self.password,
                host=self.host,
                port=self.port
            )
            return connection
        except Exception as e:
            print(f"Error connecting to database: {e}")
            return None


    def close_db(self):
        if self.connection:
            self.connection.close()


    def insert_db(self, data):
        try:
            cursor = self.connection.cursor()

            for l in data:
                song_detail = [l[0], l[2], l[3]]
                artist_detail = [l[1], l[4]]
                genre_data = l[5]

                cursor.execute("SELECT COUNT(*) FROM listened_list WHERE timestamp_column = %s", (song_detail[2],))
                timestamp_exists = cursor.fetchone()[0] > 0
                
                if timestamp_exists:
                    print(f"Timestamp {song_detail[2]} already exists. Skipping insert.")
                    continue

                cursor.execute("INSERT INTO artist (artist_name, img_url) VALUES (%s, %s) RETURNING artist_id", artist_detail)
                artist_id = cursor.fetchone()[0]

                cursor.execute(
                    "INSERT INTO listened_list (song_name, image_url, timestamp_column, artist_id) VALUES (%s, %s, %s, %s) RETURNING song_id",
                    (song_detail[0], song_detail[1], song_detail[2], artist_id)
                )
                song_id = cursor.fetchone()[0]

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
        except Exception as e:
            print(f"Error inserting data: {e}")
        finally:
            close_db()


    def get_song(self, start_date=None, end_date=None, type=None):
        try:
            cursor = self.connection.cursor()

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
        except Exception as e:
            print(f"Error fetching data: {e}")
        finally:
            close_db()

        return rows

    def get_history(self, num = 50):
        try:
            cursor = self.connection.cursor()

            cursor.execute("SELECT ll.song_name, a.artist_name, a.img_url, ll.image_url, ll.timestamp_column \
                            FROM listened_list ll \
                            INNER JOIN artist a ON ll.artist_id = a.artist_id \
                            ORDER BY ll.timestamp_column DESC LIMIT %s;", (num,))
        
            rows = cursor.fetchall()
        except Exception as e:
            print(f"Error fetching data: {e}")
        finally:
            close_db()
        return rows


    def get_genres(self):
        try:
            cursor = self.connection.cursor()

            cursor.execute("SELECT song_id, genres_id FROM song_genres;")
            rows = cursor.fetchall()

            result = []
            for(row) in rows:
                corsor.execute("SELECT song_name FROM listened_list WHERE id = %s;",(row[0],))
                song = cursor.fetchone()
                corsor.execute("SELECT genres FROM genres WHERE id = %s;",(row[1],))
                genre = cursor.fetchone()
                result.append((row[0],genre[0]))
        except Exception as e:
            print(f"Error fetching data: {e}")
        finally:
            close_db()

        return rows

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
                        artist_id INT NOT NULL,
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
                    CREATE TABLE IF NOT EXISTS artist (
                        artist_id SERIAL PRIMARY KEY,
                        artist_name TEXT NOT NULL,
                        img_url TEXT NOT NULL
                    );
                """)
                print("Table 'listened_list' created successfully.")
            cursor.close()
            connection.close()
            return table_exists
        except psycopg2.Error as e:
            print("Error connecting to the database:", e)
        finally:
            if connection:
                connection.close()