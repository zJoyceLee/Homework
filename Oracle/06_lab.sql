SYSTEM e cho '1．在SQL*Plus中使用PL/SQL块处理';
SYSTEM echo 'EMP表中职工号7788的职工，如果工资小于3000那么把工资更改为3000：';
DECLARE
x NUMBER(7, 2)
BEGIN
    SELECT sal INTO x FROM EMP WHERE empno = 7788;
    IF x < 3000 THEN
        UPDATE EMP SET sal = 3000 WHERE empno = 7788;
        END IF;
END;

SYSTEM echo '2．无参数的存储过程';
CREATE OR REPLACE PROCEDURE proc_execution
BEGIN
    UPDATE EMP SET ename = 'yourname' WHERE empno = 9010;
END proc_execution;
EXECUTE proc_execution;

SYSTEM echo '3．带输入参数的存储过程：';
SYSTEM echo '解雇给定职工号的职工，并调用proc_execution, 存储过程删除了职工号7654的职工';
CREATE OR REPLACE PROCEDURE fire_emp (val IN EMP.empno%type)
IS
BEGIN
    proc_execution;
    DELETE FROM EMP WHERE empno = val;
END fire_emp;
EXECUTE fire_emp;

SYSTEM echo '4．带输入输出的存储过程, 查询EMP中给定职工号的姓名、工资和佣金。';
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
VARIABLE emp_name VARCHAR2(15);
VARIABLE emp_sal NUMBER;
VARIABLE emp_comm NUMBER;
EXECUTE query_emp(7654, :emp_name, :emp_sal, :emp_comm);
PRINT emp_name;

SYSTEM echo '5．用Function查询出EMP中给定职工号的工资：';
CREATE OR REPLACE FUNCTION get_sal (val_empno IN EMP.empno%type)
RETURN NUMBER
IS
    val_sal EMP.sal%type := 0;
BEGIN
    SELECT sal INTO val_sal FROM EMP WHERE empno = val_empno;
    RETURN (val_sal);
END get_sal;
VARIABLE emp_sal NUMBER;
EXECUTE :emp_sal := get_sal(7654)
PRINT emp_sal;

SYSTEM echo '6．用异常处理完善程';
SYSTEM echo '如例3中：解雇给定职工号的职工，并调用proc_execution';
SYSTEM echo '如果职工号7654的职工不存在则出错。为了避免出错我们使用了EXCEPTION语句。';
CREATE OR REPLACE PROCEDURE fire_emp (val_empno IN EMP.empno%type)
IS
BEGIN
    proc_execution;
    DELETE FROM EMP WHERE empno = val_empno;
    IF SQL % NOTFOUND THEN
        RAISE_APPLICATION_ERROR(-20202, 'Employee does not exists.');
    END IF;
END fire_emp;
