WITH first AS (SELECT person_name, SUM(weight) OVER (ORDER BY turn) as sum_weight
              FROM Queue)
SELECT person_name
FROM first
WHERE sum_weight <= 1000
ORDER BY sum_weight DESC
LIMIT 1