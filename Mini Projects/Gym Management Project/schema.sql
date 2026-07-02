CREATE DATABASE gym_management;

USE gym_management;

CREATE TABLE members (
    id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    gender VARCHAR(10),
    plan VARCHAR(20),
    join_date DATE
);
