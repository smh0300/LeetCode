# Write your MySQL query statement below
WITH sub AS (SELECT product_id, min(year) as minyear
            FROM Sales
            GROUP BY product_id)
SELECT 
    sa.product_id,
    sa.year AS first_year,
    sa.quantity,
    sa.price
FROM Sales sa
LEFT JOIN sub su
ON sa.product_id = su.product_id
WHERE sa.year = su.minyear