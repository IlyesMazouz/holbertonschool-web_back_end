-- Create the users table if it doesn't exist
-- The table includes an id as primary key, email as unique, and name as a string
CREATE TABLE IF NOT EXISTS users (
  id INT AUTO_INCREMENT PRIMARY KEY,  -- id is an auto incrementing primary key
  email VARCHAR(255) NOT NULL UNIQUE,  -- email is unique and not null
  name VARCHAR(255)  -- name can be null
);
