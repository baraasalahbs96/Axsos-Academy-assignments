CREATE DATABASE normalization;
USE normalization;

CREATE TABLE dojos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255),
    location VARCHAR(255),
    created_at DATETIME,
    updated_at DATETIME
);

CREATE TABLE students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255),
    created_at DATETIME,
    updated_at DATETIME
);

CREATE TABLE addresses (
    id INT AUTO_INCREMENT PRIMARY KEY,
    address VARCHAR(255),
    student_id INT,
    FOREIGN KEY (student_id) REFERENCES students(id)
);

CREATE TABLE interests (
    id INT AUTO_INCREMENT PRIMARY KEY,
    interest VARCHAR(255),
    student_id INT,
    FOREIGN KEY (student_id) REFERENCES students(id)
);

CREATE TABLE dojo_students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    dojo_id INT,
    student_id INT,
    FOREIGN KEY (dojo_id) REFERENCES dojos(id),
    FOREIGN KEY (student_id) REFERENCES students(id)
);
