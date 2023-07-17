# Write your MySQL query statement below
WITH sub1 AS (
    SELECT requester_id , count(accepter_id) as count
    FROM RequestAccepted
    GROUP BY 1
    UNION ALL
    SELECT accepter_id, count(requester_id) as count
    FROM RequestAccepted
    GROUP BY 1
    )

SELECT requester_id as id, sum(count) as num
FROM sub1
GROUP BY 1
ORDER BY 2 DESC
LIMIT 1