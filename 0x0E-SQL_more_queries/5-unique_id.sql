-- Create a table in the db specified in cmd line
-- Create a table with unique default id field
CREATE TABLE IF NOT EXISTS unique_id (
	id INT UNIQUE DEFAULT 1,
	name VARCHAR(256)
	);
