# Write your MySQL query statement below
WITH sub1 AS (
    SELECT salary, DENSE_RANK() OVER(ORDER BY salary DESC) as ranks
    FROM Employee
    )
SELECT IFNULL(MAX(salary),NULL) as SecondHighestSalary
FROM sub1
WHERE ranks = 2