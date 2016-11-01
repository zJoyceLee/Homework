SYSTEM echo '1．创建视图, 生成一个部门号是10的视图：';
CREATE VIEW d10emp AS
SELECT empno, ename, sal FROM EMP WHERE deptno = 10;

SYSTEM echo '2．视图应用, 从视图D10EMP中查询出全部信息';
SELECT * FROM d10emp;

SYSTEM echo '3．删除视图';
DROP VIEW d10emp;

SYSTEM echo '4．创建索引';
CREATE INDEX i_ename ON EMP(ename);
CREATE UNIQUE INDEX i_empno ON EMP(empno);

SYSTEM echo '5．索引应用';
SYSTEM echo '如果查询语句如下则没有用到索引I_ENAME：';
SELECT ename, job, sal FROM EMP;
SYSTEM echo '如果查询语句如下则用到索引I_ENAME：';
SELECT * FROM EMP WHERE ename = ‘jones’;

SYSTEM echo '6．删除索引';
DROP INDEX i_ename;

SYSTEM echo '7．创建一个用户';
CREATE USER myself IDENTIFIED BY my;
SYSTEM echo '8．修用改户口令';
ALTER USER myself IDENTIFIED BY me；

SYSTEM echo '9．对象权限授权';
SYSTEM echo '把DEPT 的SELECT对象权限授给MYSELF用户：';
GRANT SELECT ON DEPT TO myself;
SYSTEM echo '把EMP的SELECT权限授给所有用户：';
GRANT SELECT ON EMP TO PUBLIC;

SYSTEM echo '10．收回对象权限';
SYSTEM echo '从MYSELF收回所有DEPT的对象权限：';
REVOKE ALL ON DEPT FROM myself；
SYSTEM echo '收回所有用户对EMP的SELECT权限：';
REVOKE SELECT ON EMP  FROM PUnnBLIC;

SYSTEM echo '11．删除用户';
DROP USER myself；
