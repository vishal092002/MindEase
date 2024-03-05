-- Create the cs491 database if not exists
CREATE DATABASE IF NOT EXISTS cs491;

-- Switch to the cs491 database
USE cs491;

-- Create the users table
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL
);
