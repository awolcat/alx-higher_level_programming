-- Query cities in California
-- Query cities table and subquery states
SELECT id, name
FROM cities
WHERE id IN (
	SELECT id
	FROM states
	WHERE name = 'California'
	)
ORDER BY id ASC;
