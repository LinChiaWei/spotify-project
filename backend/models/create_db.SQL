DROP TABLE song_genre;
DROP TABLE listened_list;
DROP TABLE genres;
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

TABLE listened_list;
TABLE genres;
TABLE song_genre;

-- SELECT *
-- FROM information_schema.constraint_column_usage
-- WHERE table_name = 'listened_list';
