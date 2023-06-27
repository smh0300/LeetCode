# Write your MySQL query statement below

WITH ordered as(
select customer_id, min(order_date) as od , min(customer_pref_delivery_date) as cd
from Delivery
group by customer_id)

select round(avg(case when od=cd then 1 else 0 end)*100,2) as immediate_percentage
from ordered