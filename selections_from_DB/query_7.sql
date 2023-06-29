SELECT subj.name, g.grade, s.fullname, grp.name
FROM grades g
LEFT JOIN subjects subj ON subj.id = g.subject_id
LEFT JOIN students s ON s.id = g.student_id
LEFT JOIN groups grp ON grp.id = s.group_id
WHERE grp.id = 1 AND subj.id = 1
GROUP BY subj.name, g.grade, s.fullname, grp.name