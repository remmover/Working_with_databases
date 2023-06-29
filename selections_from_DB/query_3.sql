SELECT subj.name, grp.name,  ROUND(AVG(g.grade), 2) as avg_grade
FROM grades g
LEFT JOIN subjects subj ON subj.id  = g.subject_id
LEFT JOIN students s ON s.id  = g.student_id
LEFT JOIN groups grp ON grp.id = s.group_id
WHERE subj.id = 2
GROUP BY subj.name, grp.name