#! /usr/bin/python3

#coding=utf-8
import MySQLdb
import random

try:
    db = MySQLdb.connect('localhost', 'root', '1', 'courseSelection', charset='utf8')
    cursor = db.cursor()

    ss = """
    SELECT semester, course_id, teacher_id, class_time
    FROM OpenCourses
    ORDER BY 1;
    """
    cursor.execute(ss)
    openCourseID = [(i[0], i[1], i[2], i[3]) for i in cursor.fetchall()]

    ss = "SELECT id FROM Students ORDER BY 1;"
    cursor.execute(ss)
    studentID = [i[0] for i in cursor.fetchall()]

    ss = """
    INSERT INTO
    SC(
    sc_semester,
    sc_course_id,
    sc_teacher_id,
    sc_class_time,
    student_id,
    grade
    ) VALUES
    """
    for i in studentID:
        for j in range(10):
            course_info = random.choice(openCourseID)
            sql = ss +"('{0}', '{1}', '{2}', '{3}', '{4}', {5});".format(
                course_info[0],
                course_info[1],
                course_info[2],
                course_info[3],
                i,
                random.randint(50, 99)
            )
            try:
                cursor.execute(sql)
                db.commit()
            except:
                db.rollback()

finally:
    db.close()
