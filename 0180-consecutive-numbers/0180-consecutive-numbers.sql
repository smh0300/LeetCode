# Write your MySQL query statement below
WITH first as (SELECT 
               num, 
               LAG(num) over () as num2, 
               LAG(num, 2) over () as num3 
               FROM Logs)
SELECT DISTINCT(num) as ConsecutiveNums
FROM first
WHERE num=num2 AND num=num3