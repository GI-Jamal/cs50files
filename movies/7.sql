SELECT M.title, R.rating
FROM ratings AS R
JOIN movies AS M
ON R.movie_id = M.id
WHERE year = 2010 AND R.rating IS NOT NULL
ORDER BY R.rating DESC, M.title ASC;