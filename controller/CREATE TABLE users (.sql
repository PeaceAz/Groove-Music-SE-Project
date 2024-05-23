CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL
);

INSERT INTO users (username, email) VALUES
    ('John_Bun', 'john@example.com'),
    ('Jude_Goat', 'jude@example.com'),
    ('Jay_Sheep', 'jay@example.com');


SELECT * FROM users;
