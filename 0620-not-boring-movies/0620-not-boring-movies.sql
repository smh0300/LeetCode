# Write your MySQL query statement below
SELECT id,movie,description,rating
FROM Cinema
WHERE description != "boring" and id%2 = 1
ORDER BY 4 DESC