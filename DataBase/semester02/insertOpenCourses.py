#! /usr/bin/python3

#coding=utf-8

import MySQLdb
import random

db = MySQLdb.connect('localhost', 'root', '1', 'courseSelection', charset='utf8')
cursor = db.cursor()

ss = """
SELECT
    Courses.id,
    Courses.name,
    Teachers.id,
    Teachers.name,
    Courses.college_name
FROM
    Courses,
    Teachers
WHERE
     Courses.college_name = Teachers.college_name;
"""
cursor.execute(ss)
results = cursor.fetchall()

# | 00830501 | 面向对象程序设计               | 10001001 | 毕丁   | 计算机工程与科学学院           |
# | 00830501 | 面向对象程序设计               | 10001018 | 袁左   | 计算机工程与科学学院           |
# | 00830501 | 面向对象程序设计               | 10001028 | 安缪   | 计算机工程与科学学院           |
# | 00830501 | 面向对象程序设计               | 10001038 | 薛汪   | 计算机工程与科学学院           |
# | 00830501 | 面向对象程序设计               | 10001053 | 喻贝   | 计算机工程与科学学院           |
# | 00830501 | 面向对象程序设计               | 10001086 | 章项   | 计算机工程与科学学院           |
# | 00830501 | 面向对象程序设计               | 10001087 | 费汲   | 计算机工程与科学学院           |
# | 00830502 | 离散数学                             | 10001001 | 毕丁   | 计算机工程与科学学院           |
# | 00830502 | 离散数学                             | 10001018 | 袁左   | 计算机工程与科学学院           |
# | 00830502 | 离散数学                             | 10001028 | 安缪   | 计算机工程与科学学院           |
# | 00830502 | 离散数学                             | 10001038 | 薛汪   | 计算机工程与科学学院           |
# | 00830502 | 离散数学                             | 10001053 | 喻贝   | 计算机工程与科学学院           |
# | 00830502 | 离散数学                             | 10001086 | 章项   | 计算机工程与科学学院           |
# | 00830502 | 离散数学                             | 10001087 | 费汲   | 计算机工程与科学学院           |


ss = """
INSERT INTO OpenCourses(semester, course_id, teacher_id, class_time) VALUES
"""
class_time = []
for i in ['星期一', '星期二', '星期三', '星期四', '星期五']:
    class_time += [
        i+j for j in ['1-2', '3-4', '5-6', '7-8']
    ]

semester = ['2015-2016秋', '2015-2016冬', '2015-2016春', '2015-2016夏']

for index, term in enumerate(semester):
     for i in range(100):
         row = random.choice(results)
         sql = ss + "('{0}', '{1}', '{2}', '{3}');".format(
             term,
             row[0],
             row[2],
             random.choice(class_time)
         )
         # print(sql)
         try:
             cursor.execute(sql)
             db.commit()
         except:
             print('OpenCourses insert error.')
             db.rollback()


ss ="""
UPDATE Students
SET name = '李羽哲', college_name = '计算机工程与科学学院'
WHERE id = '13122550';
"""
try:
    cursor.execute(ss)
    db.commit()
except:
    db.rollback()

db.close()
