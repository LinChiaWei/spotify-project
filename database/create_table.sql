CREATE TABLE IF NOT EXISTS Song_List (
    song_name TEXT NOT NULL UNIQUE,
    image_url TEXT NOT NULL,
    -- song_count INT NOT NULL,
    day_ DATE NOT NULL
);