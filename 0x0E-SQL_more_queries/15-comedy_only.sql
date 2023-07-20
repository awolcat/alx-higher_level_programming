-- Only shows of particular genre
-- Select from join that starts with table defining desired attr
SELECT title
FROM tv_genres
	LEFT OUTER JOIN tv_show_genres
		ON tv_genres.id = tv_show_genres.genre_id
	LEFT OUTER JOIN tv_shows
		ON tv_show_genres.show_id = tv_shows.id
WHERE tv_genres.name = 'Comedy'
ORDER BY title ASC;
