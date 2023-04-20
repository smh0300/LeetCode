# Write your MySQL query statement below
SELECT B.name as Customers
FROM Customers B
LEFT JOIN Orders A
ON B.id = A.customerId
WHERE A.customerId is null