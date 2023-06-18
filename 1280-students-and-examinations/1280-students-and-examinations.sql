# Write your MySQL query statement below
SELECT stu.student_id, stu.student_name, sub.subject_name, count(exam.subject_name) as attended_exams
FROM Subjects sub
CROSS JOIN Students stu
LEFT JOIN Examinations exam
ON stu.student_id = exam.student_id AND sub.subject_name = exam.subject_name
GROUP BY 1,3
ORDER BY 1,3