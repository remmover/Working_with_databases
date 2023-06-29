SELECT subj.name, t.fullname
FROM teachers t
LEFT JOIN subjects subj ON subj.teacher_id  = t.id
WHERE subj.name IS NOT NULL
GROUP BY subj.name, t.fullname