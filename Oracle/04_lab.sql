SELECT deptno, ename, mgr FROM EMP;

SELECT ename, sal + 250* 12 FROM EMP;

SELECT empno || ename AS employee FROM EMP;
SELECT empno || '-' || ename AS employee, 'works in department', deptno FROM EMP;

SELECT deptno FROM EMP;
SELECT DISTINCT deptno FROM EMP;

SELECT ename, job, sal * 12, deptno FROM EMP ORDER BY ename;
SELECT deptno, job, ename FROM EMP ORDER BY deptno, sal DESC;

SELECT ename, empno, job, deptno FROM EMP WHERE job = 'clerk';
SELECT dname, deptno FROM DEPT WHERE deptno > 20;
SELECT empno, ename, job, sal, deptno FROM EMP
WHERE sal > 1500 AND job = 'manager' OR job = 'salesman';

SELECT ename, sal FROM EMP WHERE sal BETWEEN 1000 AND 2000;
SELECT empno, ename, sal, mgr FROM EMP WHERE mgr IN (7902, 7566, 7788);
SELECT ename FROM EMP WHERE ename LIKE 's%';
SELECT ename FROM EMP WHERE ename LIKE '____';
SELECT ename FROM EMP WHERE mgr IS NULL;

SELECT empno, ename, sal FROM EMP WHERE deptno = &department_number;
SELECT empno, ename, sal * 12 FROM EMP WHERE job = '&job_title';

SELECT TO_CHAR(8897) FROM DUAL;
SELECT TO_NUMBER('8897') FROM DUAL;
SELECT TO_DATE('12-DEC-02') FROM DUAL;

SELECT AVG(sal) FROM EMP;
SELECT MIN(sal) FROM EMP WHERE job = 'clerk';
SELECT COUNT(*) FROM EMP WHERE deptno = 20;
SELECT job, AVG(sal) FROM EMP GROUP BY job;
SELECT deptno, AVG(sal) FROM EMP GROUP BY deptno HAVING COUNT(*) > 3;

SELECT ename, job, dname FROM EMP, DEPT WHERE EMP.deptno = DEPT.deptno;

SELECT ename, job, sal FROM EMP WHERE sal = (SELECT MIN(sal) FROM EMP);
SELECT ename, sal, deptno FROM EMP
WHERE sal IN (SELECT MIN(sal) FROM EMP GROUP BY deptno);
