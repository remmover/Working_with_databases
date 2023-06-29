SELECT t.fullname, s.fullname, ROUND(AVG(g.grade), 2) as avg_grade
FROM grades g
LEFT JOIN students s ON s.id = g.student_id
LEFT JOIN subjects subj ON subj.id = g.subject_id
LEFT JOIN teachers t ON t.id = subj.teacher_id
WHERE t.id = 2 AND s.id = 1
GROUP BY t.fullname, s.fullname