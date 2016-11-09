SELECT S.s#, sname FROM S, SC WHERE S.s# =  SC.s# AND c# = 'c2';

SELECT S.s#, sname FROM S, SC, C
WHERE S.s# = SC.s# AND SC.c# = C.c# AND cname = 'maths';

SELECT sname, age FROM S
WHERE s# NOT IN (SELECT s# FROM SC WHERE c# = 'c2');

SELECT sname FROM S
WHERE NOT EXiSTS (
  SELECT * FROM  C WHERE NOT EXISTS (
    SELECT * FROM SC WHERE SC.s# = S.s# AND SC.c# = C.c#
  )
);

SELECT s#, COUNT(c#), AVG(grade) FROM SC GROUP BY s#;

SELECT * FROM EMP;

SELECT empno, ename, deptno, sal FROM EMP WHERE sal BETWEEN 1000 AND 2000;

SELECT deptno, dname FROM DEPT ORDER BY 2;

SELECT DISTINCT job FROM EMP;

SELECT empno, ename FROM EMP WHERE deptno BETWEEN 10 AND 20 ORDER BY 2;

SELECT empno, ename FROM EMP WHERE deptno = 20 AND job = 'clerk';

SELECT ename FROM EMP WHERE ename LIKE '%th%' OR ename LIKE '%ll%';

SELECT ename, sal * 12 AS remuneration FROM EMP;

SELECT empno, ename FROM EMP WHERE TO_CHAR(hiredate, 'YYYY') = '1983';

SELECT  deptno, AVG(sal) FROM EMP GROUP BY deptno;

SELECT empno, ename FROM EMP WHERE sal IN (SELECT MAX(sal) FROM EMP GROUP BY deptno);

SELECT deptno, COUNT(sal) FROM EMP
WHERE sal > (SELECT AVG(sal) FROM EMP)
GROUP BY deptno;
