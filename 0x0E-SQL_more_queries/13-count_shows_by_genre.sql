-- Count tv shows by genre
-- Query genre table
SELECT name AS 'genre', COUNT(show_id) AS 'number_of_shows'
FROM tv_genres INNER JOIN tv_show_genres
	ON tv_genres.id = tv_show_genres.genre_id
GROUP BY name
ORDER BY number_of_shows DESC;
