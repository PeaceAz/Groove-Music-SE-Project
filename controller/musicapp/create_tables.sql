CREATE TABLE users (
    user_id SERIAL PRIMARY KEY,
    username VARCHAR(255) UNIQUE NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL
);

CREATE TABLE tracks (
    track_id SERIAL PRIMARY KEY,
    track_name VARCHAR(255) NOT NULL,
    artist_name VARCHAR(255) NOT NULL,
    album_name VARCHAR(255) NOT NULL,
    spotify_url VARCHAR(255) NOT NULL
);

CREATE TABLE music_history (
    history_id SERIAL PRIMARY KEY,
    user_id INT REFERENCES users(user_id),
    track_id INT REFERENCES tracks(track_id),
    listened_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE playlists (
    playlist_id SERIAL PRIMARY KEY,
    user_id INT REFERENCES users(user_id),
    playlist_name VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE playlist_tracks (
    playlist_track_id SERIAL PRIMARY KEY,
    playlist_id INT REFERENCES playlists(playlist_id),
    track_id INT REFERENCES tracks(track_id),
    added_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
