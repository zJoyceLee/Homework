#! /usr/bin/python3

#coding=utf-8
import MySQLdb
import random

try:
    db = MySQLdb.connect('localhost', 'root', '1', 'courseSelection', charset='utf8')
    cursor = db.cursor()

    ss = "SELECT id FROM OpenCourses ORDER BY 1;"
    cursor.execute(ss)
    openCourseID = [i[0] for i in cursor.fetchall()]

    ss = "SELECT id FROM Students ORDER BY 1;"
    cursor.execute(ss)
    studentID = [i[0] for i in cursor.fetchall()]

    ss = "INSERT INTO SC(id, student_id, grade) VALUES "
    for i in studentID:
        for j in range(10):
            sql = ss +"('{0}', '{1}', {2});".format(
                random.choice(openCourseID),
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
