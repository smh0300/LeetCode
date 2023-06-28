# Write your MySQL query statement below
WITH 
first AS (SELECT player_id, min(event_date) as first_date
          FROM Activity
         GROUP BY player_id),
second AS (SELECT a2.player_id, min(event_date) as second_date
          FROM Activity a2
           LEFT JOIN first f on f.player_id = a2.player_id
           WHERE a2.event_date NOT IN (f.first_date)
          GROUP BY a2.player_id)
SELECT round(avg(case when DATEDIFF(second_date,first_date) =1 then 1 else 0 end),2) as fraction
FROM first f
LEFT JOIN second s
ON f.player_id = s.player_id