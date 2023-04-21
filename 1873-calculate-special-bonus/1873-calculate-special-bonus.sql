# Write your MySQL query statement below
SELECT employee_id,
CASE 
    WHEN employee_id %2 =0 or left(name,1)='M' THEN 0
    ELSE salary
    END as bonus
FROM Employees
ORDER BY employee_id