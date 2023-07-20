-- Create a table in the db specified in cmd line
-- Create a table with not null default id field
CREATE TABLE IF NOT EXISTS id_not_null (
	id INT DEFAULT 1,
	name VARCHAR(256)
	);
