CREATE DATABASE simple_blog;
USE simple_blog;
CREATE TABLE users(
id INT AUTO_INCREMENT PRIMARY KEY,
email VARCHAR(100),
password VARCHAR(100)
);
CREATE TABLE posts(
id INT AUTO_INCREMENT PRIMARY KEY,
content TEXT,
created_at DATETIME,
user_id INT,
FOREIGN KEY (user_id) REFERENCES users(id)
);
CREATE TABLE comments(
id INT AUTO_INCREMENT PRIMARY KEY,
content TEXT,
created_at DATETIME,
user_id INT,
post_id INT,
FOREIGN KEY (user_id) REFERENCES users(id),
FOREIGN KEY (post_id) REFERENCES posts(id)
);