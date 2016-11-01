SYSTEM echo '1．对基本表S、C、SC操作';
SYSTEM echo '1）检索学习课程号为C2的学生学号与姓名。';
SELECT S.s#, sname FROM S, SC WHERE S.s# =  SC.s# AND c# = 'c2';

SYSTEM echo '2）检索选修课程名为MATHS的学生学号与姓名。';
SELECT S.s#, sname FROM S, SC, C
WHERE S.s# = SC.s# AND SC.c# = C.c# AND cname = 'maths';

SYSTEM echo '3）检索不学C2课的学生姓名与年龄。';
SELECT sname, age FROM S
WHERE s# NOT IN (SELECT s# FROM SC WHERE c# = 'c2');

SYSTEM echo '4）检索学习全部课程的学生姓名。';
SELECT sname FROM S
WHERE NOT EXiSTS (
    SELECT * FROM  C WHERE NOT EXISTS (
        SELECT * FROM SC WHERE SC.s# = S.s# AND SC.c# = C.c#
    )
);

SYSTEM echo '5）计算每个学生有成绩的课程门数和平均成绩。';
SELECT s#, COUNT(c#), AVG(grade) FROM SC GROUP BY s#;

SYSTEM echo '2．对Oracle数据库基本表EMP和DEPT操作：';
SYSTEM echo '1）检索EMP中所有的记录。';
SELECT * FROM EMP;

SYSTEM echo '2）列出工资在1000到2000之间的所有员工的ENAME，DEPTNO，SAL。';
SELECT empno, ename, deptno, sal FROM EMP WHERE sal BETWEEN 1000 AND 2000;

SYSTEM echo '3）显示DEPT表中的部门号和部门名称，并按部门名称排序。';
SELECT deptno, dname FROM DEPT ORDER BY 2;

SYSTEM echo '4）显示所有不同的工作类型。';
SELECT DISTINCT job FROM EMP;

SYSTEM echo '5）列出部门号在10到20之间的所有员工，并按名字的字母排序。';
SELECT empno, ename FROM EMP WHERE deptno BETWEEN 10 AND 20 ORDER BY 2;

SYSTEM echo '6）列出部门号是20，工作是职员的员工。';
SELECT empno, ename FROM EMP WHERE deptno = 20 AND job = 'CLERK';

SYSTEM echo '7）显示名字中包含TH和LL的员工名字。';
SELECT ename FROM EMP WHERE ename LIKE '%th%' OR ename LIKE '%ll%';

SYSTEM echo '8）显示所有员工的名字（Ename）和报酬（Remuneration）。';
SELECT ename, sal * 12 AS remuneration FROM EMP;

SYSTEM echo '9）显示在1983年中雇佣的员工。';
SELECT empno, ename FROM EMP WHERE TO_CHAR(hiredate, 'YYYY') = '1983';

SYSTEM echo '10）查询每个部门的平均工资。';
SELECT  deptno, AVG(sal) FROM EMP GROUP BY deptno;

SYSTEM echo '11）查询出每个部门中工资最高的职工。';
SELECT empno, ename FROM EMP WHERE sal IN (SELECT MAX(sal) FROM EMP GROUP BY deptno);

SYSTEM echo '12）查询出每个部门比平均工资高的职工人数。';
SELECT e.deptno, COUNT(*)
FROM
    EMP AS e,
    (SELECT deptno, AVG(sal) as avgsal FROM EMP GROUP BY deptno) AS tmpTable
WHERE
    e.deptno = tmpTable.deptno AND
    e.sal > tmpTable.avgsal
GROUP BY e.deptno;
