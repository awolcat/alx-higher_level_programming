-- Outer Join to include all tvshows
-- The outer join
SELECT title, genre_id
FROM tv_shows LEFT OUTER JOIN tv_show_genres
	ON tv_shows.id = tv_show_genres.show_id
ORDER BY title ASC, genre_id ASC;
