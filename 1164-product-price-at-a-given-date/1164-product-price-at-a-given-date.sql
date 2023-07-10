# Write your MySQL query statement below
WITH first AS (SELECT product_id, max(change_date) as max_date
                FROM Products
                WHERE change_date <= '2019-08-16'
                GROUP BY 1)
SELECT DISTINCT(p.product_id) as product_id, new_price as price
FROM Products p
RIGHT JOIN first f
ON p.product_id = f.product_id AND p.change_date = f.max_date 
GROUP BY 1
UNION
SELECT DISTINCT(product_id), 10
FROM Products
WHERE product_id NOT IN (Select product_id FROM first)