-- displays shows and their genres
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_show_genres INNER JOIN ON tv_shows.id = tv_show_genres.show_id
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;