SELECT s.fullname, g.grade
FROM grades g
JOIN students s ON s.id = g.student_id
JOIN subjects subj ON subj.id = g.subject_id
JOIN groups grp ON grp.id = s.group_id
WHERE subj.id = 1
AND grp.id = 2
AND g.date_of = (
    SELECT MAX(date_of)
    FROM grades
)