# Write your MySQL query statement below
SELECT pro.project_id, round(sum(emp.experience_years)/count(emp.experience_years),2) as average_years
FROM Project pro
LEFT JOIN Employee emp ON pro.employee_id=emp.employee_id
GROUP BY pro.project_id