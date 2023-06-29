import logging
from functools import wraps

from psycopg2 import DatabaseError

from connection import create_connection


def create_table_decorator(func):
    @wraps(func)
    def wrapper(conn, sql_expression):
        c = conn.cursor()
        try:
            func(c, sql_expression)
            conn.commit()
        except DatabaseError as e:
            logging.error(e)
            conn.rollback()
        finally:
            c.close()

    return wrapper


@create_table_decorator
def create_table(c, sql_expression):
    c.execute(sql_expression)


if __name__ == "__main__":
    sql_create_students_table = """
        CREATE TABLE IF NOT EXISTS students (
            id SERIAL PRIMARY KEY,
            fullname VARCHAR(50),
            group_id INTEGER REFERENCES groups (id)
        );
    """

    sql_create_teachers_table = """
        CREATE TABLE IF NOT EXISTS teachers (
            id SERIAL PRIMARY KEY,
            fullname VARCHAR(50)
        );
    """

    sql_create_groups_table = """
        CREATE TABLE IF NOT EXISTS groups (
            id SERIAL PRIMARY KEY,
            name VARCHAR(50) UNIQUE
        );      
    """

    sql_create_subjects_table = """
        CREATE TABLE IF NOT EXISTS subjects (
            id SERIAL PRIMARY KEY,
            name VARCHAR(50) UNIQUE,
            teacher_id INTEGER REFERENCES teachers (id)
        );
    """

    sql_create_grades_table = """
        CREATE TABLE IF NOT EXISTS grades (
            id SERIAL PRIMARY KEY,
            student_id INTEGER REFERENCES students (id),
            subject_id INTEGER REFERENCES subjects (id),
            grade INTEGER NOT NULL,
            date_of DATE
        );
    """

    try:
        with create_connection() as conn:
            if conn is not None:
                create_table(conn, sql_create_teachers_table)
                create_table(conn, sql_create_groups_table)
                create_table(conn, sql_create_subjects_table)
                create_table(conn, sql_create_students_table)
                create_table(conn, sql_create_grades_table)
            else:
                print("Error! cannot create the database connection.")
    except RuntimeError as e:
        logging.error(e)
