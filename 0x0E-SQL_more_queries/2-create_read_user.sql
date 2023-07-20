-- Create database and user with select privilege on new db
-- Create a Database
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
-- Create new user
CREATE USER IF NOT EXISTS user_0d_2@localhost
IDENTIFIED BY "user_0d_2_pwd";
-- Grant new user permissions on the new db
GRANT SELECT ON hbtn_0d_2.* TO user_0d_2@localhost;
