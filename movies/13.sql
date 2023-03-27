SELECT DISTINCT(P.name)
FROM stars AS S
JOIN people as P
ON S.person_id = P.id
JOIN movies AS M
ON S.movie_id = M.id
WHERE S.movie_id IN (SELECT movie_id FROM stars WHERE person_id = (SELECT id FROM people WHERE name = 'Kevin Bacon' AND birth = 1958)) AND NOT (P.name LIKE 'Kevin Bacon' AND P.birth = 1958);