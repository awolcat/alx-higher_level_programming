-- Join cities and states
-- Select all cities and join to states
SELECT cities.id, cities.name, states.name
FROM cities INNER JOIN states
	ON cities.state_id = states.id;
