from functools import wraps
import logging
from datetime import datetime, date, timedelta
from random import randint

from faker import Faker
from psycopg2 import DatabaseError

from creating_and_filling_DB.connection import create_connection

fake = Faker("uk-UA")

subjects = [
    "Інтернет речей",
    "Програмування мобільних пристроїв",
    "Програмування для інтернет",
    "Моделювання та аналіз програмного забезпечення",
    "Якість програмного забезпечення та тестування",
    "Операційні системи",
]

groups = ["Б-128", "Б-228", "Б-328"]

NUMBERS_TEACHERS = 5
NUMBERS_STUDENTS = 31


def create_table_decorator(func):
    @wraps(func)
    def wrapper(conn):
        c = conn.cursor()
        try:
            func(c)
            conn.commit()
        except DatabaseError as e:
            logging.error(e)
            conn.rollback()
        finally:
            c.close()

    return wrapper


@create_table_decorator
def seed_teacher(c):
    teachers = [fake.name() for _ in range(NUMBERS_TEACHERS)]
    sql = "INSERT INTO teachers(fullname) VALUES (%s);"
    c.executemany(sql, [(teacher,) for teacher in teachers])


@create_table_decorator
def seed_groups(c):
    sql = "INSERT INTO groups(name) VALUES (%s);"
    c.executemany(sql, [(group,) for group in groups])


@create_table_decorator
def seed_students(c):
    students = [fake.name() for _ in range(NUMBERS_STUDENTS)]
    list_group_id = [randint(1, len(groups)) for _ in range(NUMBERS_STUDENTS)]
    sql = "INSERT INTO students(fullname, group_id) VALUES (%s, %s);"
    c.executemany(
        sql, [(student, group_id) for student, group_id in zip(students, list_group_id)]
    )


@create_table_decorator
def seed_subjects(c):
    list_teacher_id = [randint(1, NUMBERS_TEACHERS) for _ in range(len(subjects))]
    sql = "INSERT INTO subjects(name, teacher_id) VALUES (%s, %s);"
    c.executemany(
        sql,
        [
            (subject, teacher_id)
            for subject, teacher_id in zip(subjects, list_teacher_id)
        ],
    )


@create_table_decorator
def seed_grades(c):
    start_date = datetime.strptime("2022-09-01", "%Y-%m-%d")
    finish_date = datetime.strptime("2023-05-31", "%Y-%m-%d")

    def get_list_date(start_date, finish_date) -> list[date]:
        result = []
        current_day: date = start_date.date()
        while current_day < finish_date.date():
            if current_day.isoweekday() < 6:
                result.append(current_day)
            current_day += timedelta(days=1)
        return result

    list_date = get_list_date(start_date, finish_date)

    sql = "INSERT INTO grades(student_id, subject_id, grade, date_of) VALUES (%s, %s, %s, %s);"
    for day in list_date:
        random_subject = randint(1, len(subjects))
        random_students = [randint(1, NUMBERS_STUDENTS) for _ in range(7)]
        for student in random_students:
            grade = randint(1, 12)
            c.execute(sql, (student, random_subject, grade, day))


if __name__ == "__main__":
    try:
        with create_connection() as conn:
            if conn is not None:
                seed_teacher(conn)
                seed_groups(conn)
                seed_students(conn)
                seed_subjects(conn)
                seed_grades(conn)
            else:
                print("Error! Cannot create the database connection.")
    except RuntimeError as e:
        logging.error(e)
