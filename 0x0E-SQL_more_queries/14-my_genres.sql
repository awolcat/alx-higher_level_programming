-- Dexter genre classifications
-- Query tv_shows joined to tv_show_genres and tv_genres
SELECT name
FROM tv_shows
	LEFT OUTER JOIN tv_show_genres
		ON tv_shows.id = tv_show_genres.show_id
	LEFT OUTER JOIN tv_genres
		ON tv_show_genres.genre_id = tv_genres.id
WHERE title = 'Dexter'
ORDER BY name ASC;
