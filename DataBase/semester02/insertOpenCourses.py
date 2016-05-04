#! /usr/bin/python3

#coding=utf-8

import MySQLdb
import random

db = MySQLdb.connect('localhost', 'root', '1', 'courseSelection', charset='utf8')
cursor = db.cursor()

ss = "SELECT id FROM Courses;"
cursor.execute(ss)
course_id = [_[0] for _ in cursor.fetchall()]
print(course_id)

ss = "SELECT id FROM Teachers"
cursor.execute(ss)
teacher_id = [_[0] for _ in cursor.fetchall()]
print(teacher_id)

ss = "INSERT INTO OpenCourses(semester, course_id, teacher_id, class_time, rated) VALUES"
class_time = []
for i in ['星期一', '星期二', '星期三', '星期四', '星期五']:
    class_time += [
        i+j for j in ['1-2', '3-4', '5-6', '7-8']
    ]

semester = ['2015-2016秋', '2015-2016冬', '2015-2016春', '2015-2016夏']

#     sql = ss + "('{0}', '{1}', '{2}', '{3}')".format(
#         random.choice(semester),
#         random.choice(row),
#         random.choice(teacher_id),
#         randem.choice(class_time)
#     )
#     print(sql)


db.close()
