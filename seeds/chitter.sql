DROP TABLE IF EXISTS users CASCADE;
DROP SEQUENCE IF EXISTS users_id_seq;
DROP TABLE IF EXISTS posts CASCADE;
DROP SEQUENCE IF EXISTS posts_id_seq;


-- Then, we recreate them
CREATE SEQUENCE IF NOT EXISTS users_id_seq;
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(255),
    email VARCHAR(255),
    pass VARCHAR(255)
);

CREATE SEQUENCE IF NOT EXISTS posts_id_seq;
CREATE TABLE posts (
    id SERIAL PRIMARY KEY,
    post VARCHAR(255),
    date_time TIMESTAMP,
    user_id INTEGER
);
ALTER TABLE posts
ADD CONSTRAINT fk_user
FOREIGN KEY (user_id)
REFERENCES users(id)
ON DELETE CASCADE;

INSERT INTO users (username, email, pass) VALUES ('Umut', 'umutc901@gmail.com','123');
INSERT INTO users (username, email, pass) VALUES ('calzagly', 'calzagly@gmail.com','234');

INSERT INTO posts (post, date_time,user_id) VALUES('My first post','2024-04-27 16:34:00',1);
INSERT INTO posts (post, date_time,user_id) VALUES('My second post','2024-04-27 16:50:00',1);
INSERT INTO posts (post, date_time,user_id) VALUES('My first post','2024-04-27 16:34:00',2);
INSERT INTO posts (post, date_time,user_id) VALUES('My second post','2024-04-27 16:50:00',2);

