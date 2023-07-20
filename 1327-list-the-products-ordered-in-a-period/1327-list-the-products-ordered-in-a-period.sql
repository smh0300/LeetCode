# Write your MySQL query statement below
SELECT pr.product_name, sum(unit) as unit
FROM Orders od
LEFT JOIN Products pr
ON od.product_id = pr.product_id
WHERE YEAR(order_date) = 2020 AND MONTH(order_date) = 2
GROUP BY 1
HAVING sum(unit)>=100