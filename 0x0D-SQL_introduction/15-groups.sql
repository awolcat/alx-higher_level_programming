-- Count occurences of a value
-- Count a value's occurences and output
SELECT score, COUNT(score) AS number
FROM second_table
GROUP BY score
ORDER BY number DESC;
