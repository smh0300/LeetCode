# Write your MySQL query statement below

SELECT 
    x,
    y,
    z,
    CASE WHEN (GREATEST(x,y,z)*2 - (x + y + z)) < 0
               THEN 'Yes'
               ELSE 'No'
               END AS triangle
FROM Triangle