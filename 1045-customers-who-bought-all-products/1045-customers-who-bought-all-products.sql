# Write your MySQL query statement below
with first as (select customer_id, count(distinct(product_key)) as pk
               from Customer
               group by 1),
    second as (select count(product_key) as counts
               from Product)
SELECT distinct(cu.customer_id)
FROM Customer cu
LEFT JOIN first f
ON cu.customer_id = f.customer_id
JOIN second s
WHERE f.pk = s.counts