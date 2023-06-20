# Write your MySQL query statement below
WITH 
A1 as (SELECT user_id, count(*) as allcount
       FROM Confirmations
       GROUP BY user_id),
A2 as (SELECT user_id, count(*) as confcount
       FROM Confirmations
       WHERE action="confirmed"
       GROUP BY user_id)
SELECT sign.user_id, ROUND(IFNULL((confcount/allcount),0),2) as confirmation_rate
FROM Signups sign
LEFT JOIN A1 a1 ON sign.user_id = a1.user_id
LEFT JOIN A2 a2 oN sign.user_id = a2.user_id
