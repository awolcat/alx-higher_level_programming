-- List Genres not linked to some show
-- Select from join whose base is genres
SELECT name
FROM tv_genres
WHERE tv_genres.id NOT IN (
	SELECT tv_genres.id
	FROM tv_genres
        	LEFT OUTER JOIN tv_show_genres
                	ON tv_genres.id = tv_show_genres.genre_id
        	LEFT OUTER JOIN tv_shows
                	ON tv_show_genres.show_id = tv_shows.id
	WHERE tv_shows.title = 'Dexter'
);
