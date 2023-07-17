# Write your MySQL query statement below
WITH sub1 AS (
    SELECT tiv_2015
    FROM Insurance
    GROUP BY 1
    HAVING count(*) >= 2
),
sub2 AS (
    SELECT DISTINCT lat, lon
    FROM Insurance
    GROUP BY 1,2
    HAVING count(*) = 1
)

SELECT round(sum(tiv_2016),2) as tiv_2016
FROM Insurance
WHERE tiv_2015 IN (SELECT * FROM sub1) AND
    (lat, lon) IN (SELECT * FROM sub2)