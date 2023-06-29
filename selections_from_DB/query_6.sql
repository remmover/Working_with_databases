SELECT g.name, s.fullname
FROM groups g
LEFT JOIN students s ON s.group_id  = g.id
WHERE g.id = 2
GROUP BY g.name, s.fullname