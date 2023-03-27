SELECT M.title
FROM movies as M
JOIN stars as S
ON M.id = S.movie_id
JOIN ratings as R
ON S.movie_id = R.movie_id
JOIN people as P
ON S.person_id = P.id
WHERE P.name = 'Chadwick Boseman'
ORDER BY R.rating DESC
LIMIT 5