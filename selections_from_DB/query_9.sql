SELECT subj.name, s.fullname
FROM grades g
LEFT JOIN subjects subj ON subj.id = g.subject_id
LEFT JOIN students s ON s.id = g.student_id
WHERE s.id = 11
GROUP BY subj.name, s.fullname;