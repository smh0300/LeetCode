# Please write a DELETE statement and DO NOT write a SELECT statement.
# Write your MySQL query statement below
DELETE e2 FROM Person e1, Person e2
WHERE e1.email = e2.email and e2.id > e1.id