SYSTEM echo '1．显示EMP表中所有的部门号、职工名称和管理者号码：';
SELECT deptno, ename, mgr FROM EMP;

SYSTEM echo '2. 算术运算符在SQL中的使用';
SELECT ename, sal + 250* 12 FROM EMP;

SYSTEM echo '3. 连字符的使用';
SELECT empno || ename AS employee FROM EMP;
SELECT empno || '-' || ename AS employee, 'works in department', deptno FROM EMP;

SYSTEM echo '4. 禁止重复';
SELECT deptno FROM EMP;
SELECT DISTINCT deptno FROM EMP;

SYSTEM echo '5. 排序';
SELECT ename, job, sal * 12, deptno FROM EMP ORDER BY ename;
SELECT deptno, job, ename FROM EMP ORDER BY deptno, sal DESC;

SYSTEM echo '6. 带条件的查询';
SYSTEM echo '6_1. 查询工作是CLERK的所有职工的姓名，职工号和部门号';
SELECT ename, empno, job, deptno FROM EMP WHERE job = 'CLERK';
SYSTEM echo '6_2. 从DEPT表中查询出部门号大于20的部门名称';
--Where is dname?
SELECT dname, deptno FROM DEPT WHERE deptno > 20;
SYSTEM echo '6_3. 复合条件查询';
SELECT empno, ename, job, sal, deptno FROM EMP
WHERE sal > 1500 AND job = 'MANAGER' OR job = 'SALESMAN';

SYSTEM echo '7. 操作符的应用';
SYSTEM echo '7_1. BETWEEN的应用: 查询工资在1000到2000之间的职工名字和工资信息';
SELECT ename, sal FROM EMP WHERE sal BETWEEN 1000 AND 2000;
SYSTEM echo '7_2. IN的应用: 查询有7902，7566，7788三个MGR号之一的所有职工';
SELECT empno, ename, sal, mgr FROM EMP WHERE mgr IN (7902, 7566, 7788);
SYSTEM echo '7_3_1. LIKE: 查询名字以“S”开始的所有职工: ';
SELECT ename FROM EMP WHERE ename LIKE 's%';
SYSTEM echo '7_3_2. LIKE: 查询名字只有4个字符的所有职工： ';
SELECT ename FROM EMP WHERE ename LIKE '____';
SYSTEM echo '7_4. IS NULL: 查询没有管理者的所有职工： ';
SELECT ename FROM EMP WHERE mgr IS NULL;

SYSTEM echo '8. 单&号替代变量';
SYSTEM echo '8_1. 数字变量输入: ';
SELECT empno, ename, sal FROM EMP WHERE deptno = &department_number;
SYSTEM echo '8_1. 字符串变量输入: ';
SELECT empno, ename, sal * 12 FROM EMP WHERE job = '&job_title';

--What is DUAL?
SYSTEM echo '12. 数据类型转换';
SYSTEM echo '12_1. TO_CHAR 数字数据转换为字符串';
SELECT TO_CHAR(8897) FROM DUAL;
SYSTEM echo '12_2. TO_NUMBER字符串数据转换为数字';
SELECT TO_NUMBER('8897') FROM DUAL;
SYSTEM echo '12_3. TO_DATE字符串数据转换为日期数据';
SELECT TO_DATE('12-DEC-02') FROM DUAL;

SYSTEM echo '13. 分组函数的应用';
SYSTEM echo '13_2_1. 求平均值';
SELECT AVG(sal) FROM EMP;
SYSTEM echo '13_2_2. 求最小值';
SELECT MIN(sal) FROM EMP WHERE job = 'CLERK';
SYSTEM echo '13_2_3. 求数目';
SELECT COUNT(*) FROM EMP WHERE deptno = 20;
SYSTEM echo '13_3. GROUP BY子句';
SELECT job, AVG(sal) FROM EMP GROUP BY job;
SYSTEM echo '13_3. HAVING子句';
SYSTEM echo '13_3_1. 查询人数超过3人的部门中的平均工资';
SELECT deptno, AVG(sal) FROM EMP GROUP BY deptno HAVING COUNT(*) > 3;

SYSTEM echo '14. 连接: 从EMP和DEPT中查询出职工名字、工作和部门名称';
SELECT ename, job, dname FROM EMP, DEPT WHERE EMP.deptno = DEPT.deptno;

SYSTEM echo '15. 子查询的应用:';
SYSTEM echo '15_1. 从EMP中查询出工资最低的职工:';
SELECT ename, job, sal FROM EMP WHERE sal = (SELECT MIN(sal) FROM EMP);
SYSTEM echo '15_2. 从EMP中查询出每个部门工资最低的职工：';
SELECT ename, sal, deptno FROM EMP
WHERE sal IN (SELECT MIN(sal) FROM EMP GROUP BY deptno);
