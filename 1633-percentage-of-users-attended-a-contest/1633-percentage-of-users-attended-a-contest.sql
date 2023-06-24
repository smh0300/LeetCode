# Write your MySQL query statement below
WITH all_count AS (SELECT count(DISTINCT(user_id)) as allcount from Users)
SELECT reg.contest_id, ROUND((count(DISTINCT(reg.user_id))/ac.allcount)*100,2) as percentage
FROM Register reg
JOIN all_count ac
GROUP BY contest_id
ORDER BY 2 DESC, 1