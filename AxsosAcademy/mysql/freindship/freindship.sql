-- Create database
CREATE DATABASE IF NOT EXISTS friendships_schema;
USE friendships_schema;

-- Create tables
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50)
);

CREATE TABLE friendships (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    friend_id INT,
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (friend_id) REFERENCES users(id)
);

-- Create 6 users
INSERT INTO users (first_name, last_name) VALUES
('Amy', 'Giver'),
('Eli', 'Byers'),
('Marky', 'Mark'),
('Big', 'Bird'),
('Kermit', 'The Frog'),
('Extra', 'User');

-- User 1 friends with 2, 4, 6
INSERT INTO friendships (user_id, friend_id) VALUES
(1, 2), (1, 4), (1, 6);

-- User 2 friends with 1, 3, 5
INSERT INTO friendships (user_id, friend_id) VALUES
(2, 1), (2, 3), (2, 5);

-- User 3 friends with 2 and 5
INSERT INTO friendships (user_id, friend_id) VALUES
(3, 2), (3, 5);

-- User 4 friends with 3
INSERT INTO friendships (user_id, friend_id) VALUES
(4, 3);

-- User 5 friends with 1 and 6
INSERT INTO friendships (user_id, friend_id) VALUES
(5, 1), (5, 6);

-- User 6 friends with 2 and 3
INSERT INTO friendships (user_id, friend_id) VALUES
(6, 2), (6, 3);

-- Display relationships
SELECT u1.first_name, u1.last_name, 
       u2.first_name AS friend_first_name, 
       u2.last_name AS friend_last_name
FROM users u1
JOIN friendships ON u1.id = friendships.user_id
JOIN users AS u2 ON friendships.friend_id = u2.id;

-- NINJA 1: Friends of user 1
SELECT u2.first_name AS friend_first_name, u2.last_name AS friend_last_name
FROM users u1
JOIN friendships ON u1.id = friendships.user_id
JOIN users AS u2 ON friendships.friend_id = u2.id
WHERE u1.id = 1;

-- NINJA 2: Count of all friendships
SELECT COUNT(*) AS total_friendships FROM friendships;

-- NINJA 3: Who has the most friends
SELECT u1.first_name, u1.last_name, COUNT(*) AS friend_count
FROM users u1
JOIN friendships ON u1.id = friendships.user_id
GROUP BY u1.id
ORDER BY friend_count DESC
LIMIT 1;

-- NINJA 4: Friends of user 3 in alphabetical order
SELECT u2.first_name AS friend_first_name, u2.last_name AS friend_last_name
FROM users u1
JOIN friendships ON u1.id = friendships.user_id
JOIN users AS u2 ON friendships.friend_id = u2.id
WHERE u1.id = 3
ORDER BY u2.first_name ASC;