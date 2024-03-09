DROP TABLE song_genre;
DROP TABLE listened_list;
DROP TABLE genres;
DROP TABLE artist;

CREATE TABLE IF NOT EXISTS artist (
    artist_id SERIAL PRIMARY KEY,
    artist_name TEXT NOT NULL,
    img_url TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS listened_list (
    song_id SERIAL PRIMARY KEY,
    song_name TEXT NOT NULL,
    artist_id INT NOT NULL ,
    image_url TEXT NOT NULL,
    timestamp_column TIMESTAMP NOT NULL,
    FOREIGN KEY(artist_id) REFERENCES artist(artist_id)
);
CREATE TABLE IF NOT EXISTS genres (
    genre_id SERIAL PRIMARY KEY,
    genre TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS song_genre (
    song_id INT,
    genre_id INT,
    FOREIGN KEY(song_id) REFERENCES listened_list(song_id),
    FOREIGN KEY(genre_id) REFERENCES genres(genre_id)
);



TABLE listened_list;
TABLE genres;
TABLE song_genre;
TABLE artist;

-- SELECT *
-- FROM information_schema.constraint_column_usage
-- WHERE table_name = 'listened_list';
