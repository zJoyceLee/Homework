SYSTEM echo '1. INSERT';
INSERT INTO S(s#, sname, age, sex) VALUES ('s1', 'wang', 20, 'M');
INSERT INTO S(s#, sname, age, sex) VALUES ('s2', 'liu', 19, 'M');
INSERT INTO S(s#, sname, age, sex) VALUES ('s3', 'chen', 22, 'M');
INSERT INTO S(s#, sname, age, sex) VALUES ('s4', 'wu', 19, 'M');
INSERT INTO S(s#, sname, age, sex) VALUES ('s5', 'lou', 21, 'F');
INSERT INTO S(s#, sname, age, sex) VALUES ('s8', 'dong', 18, 'F');

INSERT INTO C(c#, cname, teacher) VALUES ('c2', 'maths', 'ma');
INSERT INTO C(c#, cname, teacher) VALUES ('c4', 'physics', 'shi');
INSERT INTO C(c#, cname, teacher) VALUES ('c3', 'chemistry', 'zhou');
INSERT INTO C(c#, cname, teacher) VALUES ('c1', 'db', 'li');
INSERT INTO C(c#, cname, teacher) VALUES ('c5', 'os', 'wen');

INSERT INTO SC(s#, c#, grade) VALUES ('s1', 'c1', 80);
INSERT INTO SC(s#, c#, grade) VALUES ('s1', 'c2', 70);
INSERT INTO SC(s#, c#, grade) VALUES ('s1', 'c3', 85);
INSERT INTO SC(s#, c#, grade) VALUES ('s1', 'c4', 90);
INSERT INTO SC(s#, c#, grade) VALUES ('s1', 'c5', 70);
INSERT INTO SC(s#, c#, grade) VALUES ('s2', 'c1', 85);
INSERT INTO SC(s#, c#) VALUES ('s2', 'c2');
INSERT INTO SC(s#, c#) VALUES ('s2', 'c4');
INSERT INTO SC(s#, c#, grade) VALUES ('s3', 'c1', 90);
INSERT INTO SC(s#, c#, grade) VALUES ('s3', 'c2', 85);
INSERT INTO SC(s#, c#, grade) VALUES ('s3', 'c3', 95);
INSERT INTO SC(s#, c#, grade) VALUES ('s4', 'c1', 75);
INSERT INTO SC(s#, c#) VALUES ('s4', 'c3');
INSERT INTO SC(s#, c#, grade) VALUES ('s4', 'c4', 70);
INSERT INTO SC(s#, c#, grade) VALUES ('s5', 'c1', 70);
INSERT INTO SC(s#, c#, grade) VALUES ('s5', 'c2', 60);
INSERT INTO SC(s#, c#, grade) VALUES ('s5', 'c3', 80);
INSERT INTO SC(s#, c#, grade) VALUES ('s5', 'c5', 65);
INSERT INTO SC(s#, c#, grade) VALUES ('s5', 'c1', 90);
INSERT INTO SC(s#, c#) VALUES ('s5', 'c2');
INSERT INTO SC(s#, c#, grade) VALUES ('s5', 'c3', 90);
INSERT INTO SC(s#, c#) VALUES ('s5', 'c5');

SELECT * FORM S;
SELECT * FROM C;
SELECT * FORM SC;

SYSTEM echo '2_1. 把C2非空成绩提高10%';
UPDATE SC SET grade = grade * 1.1 WHERE c# = 'c2' AND grade IS NOT NULL;
SYSTEM echo '2_2. 在SC表中删除课程名为PHYSICS的成绩元组';
DELETE FROM SC WHERE c# = (SELECT c# FROM C WHERE cname = 'physics');
SYSTEM echo '2_3. 在S和SC表中删除学号为s8的所有数据'；
DELETE FROM SC WHERE s# = 's8';
DELETE FROM S WHERE s# = 's8';

SYSTEM echo '3. 在PROJECTS中添加记录';
INSERT INTO PROJECTS VALUES (1, 'write c030 course', '02-JAN-88', '07-JAN-88', 500, 1, 'br_creative');
INSERT INTO PROJECTS VALUES (2, 'proof read notes', '01-JAN-89', '10-JAN-89', 600, 1, 'your choice');

SYSTEM echo '4. 在ASSIGNMENTS表中添加记录';
INSERT INTO ASSIGNMENTS VALUES(1, 7369, '01-JAN-88', '03-JAN-88', 50.00, 'WR', 15);
INSERT INTO ASSIGNMENTS VALUES(2, 7844, '01-JAN-89', '10-JAN-89', 45.50, 'PF', 30);

SYSTEM echo '5. 把ASSIGNMENTS表中ASSIGNMENT TYPE 的WR改为WT， 其他值不变';
UPDATE ASSIGNMENTS SET assign_type = 'WT' WHERE assign_type = 'WR';

SYSTEM echo '6. 在PROJECTS和ASSIGNMENTS随便添加一些数据并删除';
SELECT * FROM PROJECTS;
INSERT INTO PROJECTS VALUES(3, 'str', '29-Apr-16','28-Feb-17', 300, 1, 'comment');
SELECT * FROM PROJECTS;
DELETE FROM PROJECTS WHERE projid = 3;

SELECT * FROM ASSIGNMENTS;
INSERT INTO ASSIGNMENTS VALUES(3, 7844, '01-JAN-89', '10-JAN-89', 45.50, 'PF', 30);
SELECT * FROM ASSIGNMENTS;
DELETE FROM ASSIGNMENTS WHERE projid = 3 AND empno = 7844;
