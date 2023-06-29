import logging

from psycopg2 import DatabaseError

from creating_and_filling_DB.connection import create_connection

if __name__ == '__main__':
    sql_expression1 = """
        SELECT s.fullname, ROUND(AVG(g.grade), 2) as avg_grade
        FROM grades g 
        LEFT JOIN students s ON s.id = g.student_id 
        GROUP BY s.id
        ORDER BY avg_grade DESC
        LIMIT 5;
    """

    sql_expression2 = """
        SELECT sbj.name, s.fullname, ROUND(AVG(g.grade), 2) as avg_grade
        FROM grades g 
        LEFT JOIN students s ON s.id = g.student_id 
        LEFT JOIN subjects sbj ON sbj.id = g.subject_id 
        WHERE sbj.id = 1
        GROUP BY sbj.name, s.fullname
        ORDER BY avg_grade DESC
        LIMIT 1;
    """

    sql_expression3 = """
        SELECT subj.name, grp.name,  ROUND(AVG(g.grade), 2) as avg_grade
        FROM grades g
        LEFT JOIN subjects subj ON subj.id  = g.subject_id
        LEFT JOIN students s ON s.id  = g.student_id
        LEFT JOIN groups grp ON grp.id = s.group_id
        WHERE subj.id = 2
        GROUP BY subj.name, grp.name
    """

    sql_expression4 = """
        SELECT ROUND(AVG(g.grade), 2) as avg_grade
        FROM grades g
    """

    sql_expression5 = """
        SELECT subj.name, t.fullname
        FROM teachers t
        LEFT JOIN subjects subj ON subj.teacher_id  = t.id
        WHERE subj.name IS NOT NULL 
        GROUP BY subj.name, t.fullname
    """

    sql_expression6 = """
        SELECT g.name, s.fullname
        FROM groups g
        LEFT JOIN students s ON s.group_id  = g.id
        WHERE g.id = 2
        GROUP BY g.name, s.fullname
    """

    sql_expression7 = """
        SELECT subj.name, g.grade, s.fullname, grp.name
        FROM grades g 
        LEFT JOIN subjects subj ON subj.id = g.subject_id
        LEFT JOIN students s ON s.id = g.student_id
        LEFT JOIN groups grp ON grp.id = s.group_id
        WHERE grp.id = 1 AND subj.id = 1
        GROUP BY subj.name, g.grade, s.fullname, grp.name
    """

    sql_expression8 = """
        SELECT t.fullname, subj.name, ROUND(AVG(g.grade), 2) as avg_grade
        FROM grades g
        LEFT JOIN subjects subj ON subj.id = g.subject_id
        LEFT JOIN teachers t ON t.id = subj.teacher_id
        WHERE t.id = 4
        GROUP BY subj.name, t.fullname
    """

    sql_expression9 = """
        SELECT subj.name, s.fullname
        FROM grades g
        LEFT JOIN subjects subj ON subj.id = g.subject_id
        LEFT JOIN students s ON s.id = g.student_id
        WHERE s.id = 11
        GROUP BY subj.name, s.fullname;
    """

    # Список курсів, які певному студенту читає певний викладач.
    sql_expression10 = """
        SELECT subj.name, s.fullname, t.fullname
        FROM grades g
        LEFT JOIN students s ON s.id = g.student_id
        LEFT JOIN subjects subj ON subj.id = g.subject_id
        LEFT JOIN teachers t ON t.id = subj.teacher_id
        WHERE t.id = 2 AND s.id = 1
        GROUP BY subj.name, s.fullname, t.fullname
    """

    # Середній бал, який певний викладач ставить певному студентові.
    sql_expression11 = """
        SELECT t.fullname, s.fullname, ROUND(AVG(g.grade), 2) as avg_grade
        FROM grades g
        LEFT JOIN students s ON s.id = g.student_id
        LEFT JOIN subjects subj ON subj.id = g.subject_id
        LEFT JOIN teachers t ON t.id = subj.teacher_id
        WHERE t.id = 2 AND s.id = 1
        GROUP BY t.fullname, s.fullname
    """

    # Оцінки студентів у певній групі з певного предмета на останньому занятті.
    sql_expression12 = """
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
    """

    try:
        with create_connection() as conn:
            if conn is not None:
                c = conn.cursor()
                try:
                    c.execute(sql_expression1)
                    print(c.fetchall())

                    c.execute(sql_expression2)
                    print(c.fetchall())

                    c.execute(sql_expression3)
                    print(c.fetchall())

                    c.execute(sql_expression4)
                    print(c.fetchall())

                    c.execute(sql_expression5)
                    print(c.fetchall())

                    c.execute(sql_expression6)
                    print(c.fetchall())

                    c.execute(sql_expression7)
                    print(c.fetchall())

                    c.execute(sql_expression8)
                    print(c.fetchall())

                    c.execute(sql_expression9)
                    print(c.fetchall())

                    c.execute(sql_expression10)
                    print(c.fetchall())

                    c.execute(sql_expression11)
                    print(c.fetchall())

                    c.execute(sql_expression12)
                    print(c.fetchall())

                except DatabaseError as e:
                    logging.error(e)
                finally:
                    c.close()
            else:
                print("Error! cannot create the database connection.")
    except RuntimeError as e:
        logging.error(e)
