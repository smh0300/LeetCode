# Write your MySQL query statement below
WITH sub1 as (
    SELECT *, DENSE_RANK() OVER(PARTITION BY departmentId ORDER BY salary DESC) as rk
    FROM Employee
    )
SELECT de.name as Department, s1.name as Employee, s1.salary as Salary
FROM sub1 s1
LEFT JOIN Department de
ON s1.departmentId = de.id
WHERE rk <= 3