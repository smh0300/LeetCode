# Write your MySQL query statement below
with first as (SELECT count(*) as reports_count, round(avg(age),0) as average_age, reports_to
                FROM Employees
                WHERE reports_to IS NOT NULL
                GROUP BY reports_to)
SELECT employee_id, name, reports_count, average_age
FROM first fr
LEFT JOIN Employees em 
ON em.employee_id = fr.reports_to
ORDER BY 1