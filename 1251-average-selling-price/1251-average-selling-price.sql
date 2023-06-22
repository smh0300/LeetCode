# Write your MySQL query statement below
SELECT price.product_id, round(sum(price * units)/ sum(units),2) as average_price
FROM Prices price
LEFT JOIN UnitsSold unit
ON price.product_id = unit.product_id 
AND price.start_date <= unit.purchase_date
AND price.end_date >= unit.purchase_date
GROUP BY price.product_id