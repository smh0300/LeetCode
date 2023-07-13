# Write your MySQL query statement below
SELECT id, IFNULL((CASE WHEN id % 2 = 1 
            THEN LEAD(student) OVER ()
           ELSE LAG(student) OVER ()
           END),student) as student
FROM Seat