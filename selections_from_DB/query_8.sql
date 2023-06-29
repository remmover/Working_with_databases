SELECT t.fullname, subj.name, ROUND(AVG(g.grade), 2) as avg_grade
FROM grades g
LEFT JOIN subjects subj ON subj.id = g.subject_id
LEFT JOIN teachers t ON t.id = subj.teacher_id
WHERE t.id = 4
GROUP BY subj.name, t.fullname