# Write your MySQL query statement below
WITH sub1 AS (
        SELECT user_id, RANK() OVER(ORDER BY count(DISTINCT(movie_id)) DESC) as rank123
        FROM MovieRating
        GROUP BY 1
            ),
    sub2 AS (
        SELECT movie_id, created_at, RANK() OVER(ORDER BY avg(rating) DESC) as average
        FROM MovieRating
        GROUP BY movie_id, MONTH(created_at)
        HAVING YEAR(created_at)=2020 AND MONTH(created_at)=2
        )
 
(SELECT name as results
FROM Users
WHERE user_id in (SELECT user_id 
                  FROM sub1 
                  WHERE rank123 = 1)
ORDER BY 1
LIMIT 1)
UNION ALL
(SELECT title
FROM Movies
WHERE movie_id IN (SELECT movie_id
                   FROM sub2
                   WHERE average = 1)
ORDER BY 1
LIMIT 1)