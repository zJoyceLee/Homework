INSERT INTO DEPT(deptno, dname) VALUES (10, 'accounting');
INSERT INTO DEPT(deptno, dname) VALUES (20, 'research');
INSERT INTO DEPT(deptno, dname) VALUES (30, 'sales');
INSERT INTO DEPT(deptno, dname) VALUES (40, 'operations');
SELECT * FROM DEPT;

INSERT INTO EMP(empno, ename, job, mgr, hiredate, sal, deptno) VALUES
(7369, 'smith', 'clerk', 7902, TO_DATE('1980-12-17', 'yyyy-mm-dd'), 800, 20);
INSERT INTO EMP(empno, ename, job, mgr, hiredate, sal, comm, deptno) VALUES
(7499, 'allen', 'salesman', 7698, TO_DATE('1981-02-20', 'yyyy-mm-dd'), 1600, 300, 30);
INSERT INTO EMP(empno, ename, job, mgr, hiredate, sal, comm, deptno) VALUES
(7521, 'ward', 'salesman', 7698, TO_DATE('1981-02-22', 'yyyy-mm-dd'), 1250, 500, 30);
INSERT INTO EMP(empno, ename, job, mgr, hiredate, sal, deptno) VALUES
(7566, 'jones', 'manager', 7839, TO_DATE('1981-04-02', 'yyyy-mm-dd'), 2975, 20);
INSERT INTO EMP(empno, ename, job, mgr, hiredate, sal, comm, deptno) VALUES
(7654, 'martin', 'salesman', 7698, TO_DATE('1981-09-28', 'yyyy-mm-dd'), 1250, 1400, 30);
INSERT INTO EMP(empno, ename, job, mgr, hiredate, sal, deptno) VALUES
(7698, 'blake', 'manager', 7839, TO_DATE('1981-05-01', 'yyyy-mm-dd'), 2850, 30);
INSERT INTO EMP(empno, ename, job, mgr, hiredate, sal, deptno) VALUES
(7782, 'clark', 'manager', 7839, TO_DATE('1981-06-09', 'yyyy-mm-dd'), 2450, 10);
INSERT INTO EMP(empno, ename, job, mgr, hiredate, sal, deptno) VALUES
(7788, 'scott', 'analyst', 7566, TO_DATE('1987-04-19', 'yyyy-mm-dd'), 3000, 20);
INSERT INTO EMP(empno, ename, job, hiredate, sal, deptno) VALUES
(7839, 'king', 'president', TO_DATE('1981-11-17', 'yyyy-mm-dd'), 5000, 10);
INSERT INTO EMP(empno, ename, job, mgr, hiredate, sal, comm, deptno) VALUES
(7844, 'turner', 'salesman', 7698, TO_DATE('1981-09-08', 'yyyy-mm-dd'), 1500, 0, 30);
INSERT INTO EMP(empno, ename, job, mgr, hiredate, sal, deptno) VALUES
(7876, 'adams', 'clerk', 7788, TO_DATE('1987-05-23', 'yyyy-mm-dd'), 1100, 20);
INSERT INTO EMP(empno, ename, job, mgr, hiredate, sal, deptno) VALUES
(7900, 'james', 'clerk', 7698, TO_DATE('1981-12-03', 'yyyy-mm-dd'), 950, 30);
INSERT INTO EMP(empno, ename, job, mgr, hiredate, sal, deptno) VALUES
(8902, 'ford', 'analyst', 7566, TO_DATE('1981-12-02', 'yyyy-mm-dd'), 3000, 20);
INSERT INTO EMP(empno, ename, job, mgr, hiredate, sal, deptno) VALUES
(7934, 'miller', 'clerk', 7782, TO_DATE('1982-01-27', 'yyyy-mm-dd'), 1300, 10);
SELECT  * FROM EMP;

INSERT INTO STATE(state_name, state_id) VALUES ('Massachusetts', 'MA');
INSERT INTO STATE(state_name, state_id) VALUES ('California', 'CA');
INSERT INTO STATE(state_name, state_id) VALUES ('NewJersey', 'NJ');
INSERT INTO STATE(state_name, state_id) VALUES ('New York', 'NY');
SELECT * FROM STATE;
UPDATE STATE SET state_name = 'Florida', state_id = 'FD'
WHERE state_name = 'New York' AND state_id = 'NY';
SELECT * FROM STATE;

DELETE FROM STATE WHERE state_name = 'Florida' AND state_id = 'FD';
SELECT * FROM STATE;

INSERT INTO CUSTOMER VALUES ('Nicholson', 'CA', 6989.99);
INSERT INTO CUSTOMER VALUES ('Martin', 'CA', 2345.45);
INSERT INTO CUSTOMER VALUES ('Laursen', 'CA', 34.34);
INSERT INTO CUSTOMER VALUES ('Bambi', 'CA', 1234.55);
INSERT INTO CUSTOMER VALUES ('McGraw', 'NJ', 123.45);
SELECT * FROM CUSTOMER;

INSERT INTO S(s#, sname, age, sex) VALUES ('s1', 'wang', 20, 'M');
INSERT INTO S(s#, sname, age, sex) VALUES ('s2', 'liu', 19, 'M');
INSERT INTO S(s#, sname, age, sex) VALUES ('s3', 'chen', 22, 'M');
INSERT INTO S(s#, sname, age, sex) VALUES ('s4', 'wu', 19, 'M');
INSERT INTO S(s#, sname, age, sex) VALUES ('s5', 'lou', 21, 'F');
INSERT INTO S(s#, sname, age, sex) VALUES ('s8', 'dong', 18, 'F');
SELECT * FROM S;

INSERT INTO C(c#, cname, teacher) VALUES ('c2', 'maths', 'ma');
INSERT INTO C(c#, cname, teacher) VALUES ('c4', 'physics', 'shi');
INSERT INTO C(c#, cname, teacher) VALUES ('c3', 'chemistry', 'zhou');
INSERT INTO C(c#, cname, teacher) VALUES ('c1', 'db', 'li');
INSERT INTO C(c#, cname, teacher) VALUES ('c5', 'os', 'wen');
SELECT * FROM C;

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
INSERT INTO SC(s#, c#, grade) VALUES ('s8', 'c1', 90);
INSERT INTO SC(s#, c#) VALUES ('s8', 'c2');
INSERT INTO SC(s#, c#, grade) VALUES ('s8', 'c3', 90);
INSERT INTO SC(s#, c#) VALUES ('s8', 'c5');
SELECT * FROM SC;


UPDATE SC SET grade = grade * 1.1 WHERE c# = 'c2' AND grade IS NOT NULL;
DELETE FROM SC WHERE c# = (SELECT c# FROM C WHERE cname = 'physics');
DELETE FROM SC WHERE s# = 's8';
DELETE FROM S WHERE s# = 's8';

INSERT INTO PROJECTS VALUES (1, 'write c030 course', '02-JAN-88', '07-JAN-88', 500, 1, 'br_creative');
INSERT INTO PROJECTS VALUES (2, 'proof read notes', '01-JAN-89', '10-JAN-89', 600, 1, 'your choice');

INSERT INTO ASSIGNMENTS VALUES(1, 7369, '01-JAN-88', '03-JAN-88', 50.00, 'WR', 15);
INSERT INTO ASSIGNMENTS VALUES(2, 7844, '01-JAN-89', '10-JAN-89', 45.50, 'PF', 30);

UPDATE ASSIGNMENTS SET assign_type = 'WT' WHERE assign_type = 'WR';

SELECT * FROM PROJECTS;
INSERT INTO PROJECTS VALUES(3, 'str', '29-Apr-16','28-Feb-17', 300, 1, 'comment');
SELECT * FROM PROJECTS;

SELECT * FROM ASSIGNMENTS;
INSERT INTO ASSIGNMENTS VALUES(3, 7844, '01-JAN-89', '10-JAN-89', 45.50, 'PF', 30);
SELECT * FROM ASSIGNMENTS;

DELETE FROM ASSIGNMENTS WHERE projid = 3 AND empno = 7844;
DELETE FROM PROJECTS WHERE projid = 3;
