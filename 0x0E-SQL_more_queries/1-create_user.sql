-- Create a new user
-- Create User and set password
CREATE USER IF NOT EXISTS user_0d_1@localhost
IDENTIFIED BY "user_0d_1_pwd";
-- Grant global privilleges to new user
GRANT ALL ON *.* TO user_0d_1@localhost;
