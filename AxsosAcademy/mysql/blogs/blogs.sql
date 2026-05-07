CREATE DATABASE blogs_app;
USE blogs_app;

CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100)
);

CREATE TABLE blogs (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    user_id INT,
    FOREIGN KEY (user_id) REFERENCES users(id)
);

CREATE TABLE blog_admins (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    blog_id INT,
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (blog_id) REFERENCES blogs(id)
);

CREATE TABLE posts (
    id INT AUTO_INCREMENT PRIMARY KEY,
    content TEXT,
    blog_id INT,
    user_id INT,
    FOREIGN KEY (blog_id) REFERENCES blogs(id),
    FOREIGN KEY (user_id) REFERENCES users(id)
);

CREATE TABLE comments (
    id INT AUTO_INCREMENT PRIMARY KEY,
    content TEXT,
    post_id INT,
    user_id INT,
    FOREIGN KEY (post_id) REFERENCES posts(id),
    FOREIGN KEY (user_id) REFERENCES users(id)
);

CREATE TABLE page_visits (
    id INT AUTO_INCREMENT PRIMARY KEY,
    page VARCHAR(255),
    visited_at DATETIME,
    duration INT,
    ip_address VARCHAR(50),
    user_id INT,
    FOREIGN KEY (user_id) REFERENCES users(id)
);
