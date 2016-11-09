SELECT empno, ename, sal FROM EMP WHERE empno = 7788;
UPDATE EMP SET sal = 200 WHERE empno = 7788;
SELECT empno, ename, sal FROM EMP WHERE empno = 7788;
DECLARE
x NUMBER(7, 2);
BEGIN
    SELECT sal INTO x FROM EMP WHERE empno = 7788;
    IF x < 3000 THEN
        UPDATE EMP SET sal = 3000 WHERE empno = 7788;
        END IF;
END;
/
SELECT empno, ename, sal FROM EMP WHERE empno = 7788;



SELECT empno, ename, sal FROM EMP WHERE empno = 9010;
CREATE OR REPLACE PROCEDURE proc_execution
IS
BEGIN
    UPDATE EMP SET ename = 'yourname' WHERE empno = 9010;
END proc_execution;
/
EXECUTE proc_execution;
SELECT empno, ename, sal FROM EMP WHERE empno = 9010;



SELECT empno, ename, sal FROM EMP ORDER BY 1;
CREATE OR REPLACE PROCEDURE fire_emp (val IN EMP.empno%type)
IS
BEGIN
    proc_execution;
    DELETE FROM EMP WHERE empno = val;
END fire_emp;
/
EXECUTE fire_emp(7654);
SELECT empno, ename, sal FROM EMP ORDER BY 1;

INSERT INTO EMP(empno, ename, job, mgr, hiredate, sal, comm, deptno) VALUES
(7654, 'martin', 'salesman', 7698, TO_DATE('1981-09-28', 'yyyy-mm-dd'), 1250, 1400, 30);


CREATE OR REPLACE PROCEDURE query_emp (
    val_empno IN EMP.empno%type,
    val_ename OUT EMP.ename%type,
    val_sal OUT EMP.sal%type,
    val_comm OUT EMP.comm%type
) IS
BEGIN
    SELECT ename, sal, comm INTO val_ename, val_sal, val_comm
    FROM EMP WHERE empno = val_empno;
END query_emp;
/
VARIABLE emp_name VARCHAR2(15);
VARIABLE emp_sal NUMBER;
VARIABLE emp_comm NUMBER;
EXECUTE query_emp(7654, :emp_name, :emp_sal, :emp_comm);
PRINT emp_name;

CREATE OR REPLACE FUNCTION get_sal (val_empno IN EMP.empno%type)
RETURN NUMBER
IS
    val_sal EMP.sal%type := 0;
BEGIN
    SELECT sal INTO val_sal FROM EMP WHERE empno = val_empno;
    RETURN (val_sal);
END get_sal;
/
VARIABLE emp_sal NUMBER;
EXECUTE :emp_sal := get_sal(7654)
PRINT emp_sal;

CREATE OR REPLACE PROCEDURE fire_emp (val_empno IN EMP.empno%type)
IS
BEGIN
    proc_execution;
    DELETE FROM EMP WHERE empno = val_empno;
    IF SQL % NOTFOUND THEN
        RAISE_APPLICATION_ERROR(-20202, 'Employee does not exists.');
    END IF;
END fire_emp;
/
