-- This script creates the 'users' table if it does not already exist
-- It ensures that the 'email' column is unique to avoid duplicate entries

CREATE TABLE
IF NOT EXISTS users
(
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR
(255) NOT NULL UNIQUE,
    name VARCHAR
(255)
);
