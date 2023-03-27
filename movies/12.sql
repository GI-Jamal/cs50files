SELECT M.title
FROM stars AS S
JOIN people as P
ON S.person_id = P.id
JOIN movies as M
ON M.id = S.movie_id
WHERE name = 'Johnny Depp' OR name = 'Helena Bonham Carter'
GROUP BY M.title
HAVING COUNT(M.title) = 2;