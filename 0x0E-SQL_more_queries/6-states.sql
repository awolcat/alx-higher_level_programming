-- Create new database and table in new db
-- Create the database
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- Use correct db
USE hbtn_0d_usa;
-- Create Table in the db
CREATE TABLE IF NOT EXISTS states (
	id INT UNIQUE NOT NULL AUTO_INCREMENT PRIMARY KEY,
	name VARCHAR(256) NOT NULL
);

