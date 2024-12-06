-- Create the users table if it doesn't exist
-- The table includes an id as primary key, email as unique, and name as a string

CREATE TABLE IF NOT EXISTS users (
  id INT AUTO_INCREMENT PRIMARY KEY,
  email VARCHAR(255) NOT NULL UNIQUE,
  name VARCHAR(255)
);
