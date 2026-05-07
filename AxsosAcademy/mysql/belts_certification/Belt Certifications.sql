CREATE DATABASE belts_certification;
USE belts_certification;

CREATE TABLE students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100)
);

CREATE TABLE belts (
    id INT AUTO_INCREMENT PRIMARY KEY,
    color VARCHAR(50)
);

CREATE TABLE certifications (
    id INT AUTO_INCREMENT PRIMARY KEY,
    student_id INT,
    belt_id INT,
    FOREIGN KEY (student_id) REFERENCES students(id),
    FOREIGN KEY (belt_id) REFERENCES belts(id)
);
