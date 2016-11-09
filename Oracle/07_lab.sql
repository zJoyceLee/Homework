SET SERVEROUTPUT ON;

DECLARE
    CURSOR c1 IS
        SELECT ename, sal, hiredate FROM EMP WHERE deptno = 20 AND  job = 'analyst';
    v_name      EMP.ename%TYPE;
    v_sal           EMP.sal%TYPE;
    v_hiredate  EMP.hiredate%TYPE;

    CURSOR c2 IS
        SELECT * FROM EMP WHERE deptno = 20 AND job = 'analyst';
    v_emp EMP%ROWTYPE;
    v_count NUMBER := 0;
BEGIN
    DBMS_OUTPUT.PUT_LINE('Q1:');

    OPEN c1;
    FETCH c1 INTO v_name, v_sal, v_hiredate;
    IF c1%FOUND THEN
    DBMS_OUTPUT.PUT_LINE(
        'name: ' || v_name ||
        ', salary: '  || v_sal ||
        ', hire date: '  || v_hiredate);
    END IF;
    CLOSE c1;

    DBMS_OUTPUT.PUT_LINE('Q2.1:');

    IF c2%ISOPEN THEN
        FETCH c2 INTO v_emp;
        DBMS_OUTPUT.PUT_LINE('-----cursor already open.-----');
    ELSE
        OPEN c2;
        DBMS_OUTPUT.PUT_LINE('-----open c2.-----');
    END IF;

    LOOP
        FETCH c2 INTO v_emp;
        IF c2%NOTFOUND THEN
            EXIT;
        ELSE
            DBMS_OUTPUT.PUT_LINE(
                'name: ' || v_emp.ename ||
                ', salary: '  || v_emp.sal ||
                ', hire date: '  || v_emp.hiredate);
        END IF;
    END LOOP;
    CLOSE c2;
END;
/

UPDATE EMP SET sal = 1000 WHERE empno = 7788;
SELECT empno, sal, hiredate FROM EMP WHERE deptno = 20 AND job = 'analyst';
DECLARE
    CURSOR c3 IS
    SELECT empno, sal, hiredate, rowid
    FROM EMP WHERE deptno = 20 AND job = 'analyst'
    FOR UPDATE OF sal;
    EMP_record c3%ROWTYPE;
BEGIN
    DBMS_OUTPUT.PUT_LINE('Q2.2:');
    OPEN c3;
    LOOP
        FETCH c3 INTO EMP_record;
        IF c3%NOTFOUND THEN
            EXIT;
        ELSE
            IF EMP_record.sal < 2000 THEN
                 UPDATE EMP SET sal = 2000 WHERE empno = EMP_record.empno;
            END IF;
        END IF;
    END LOOP;
    CLOSE c3;
    COMMIT;
END;
/
SELECT empno, sal, hiredate FROM EMP WHERE deptno = 20 AND job = 'analyst';


CREATE TABLE COUNTS(
    sales_set NUMBER,
    non_sales_set NUMBER
);
DESCRIBE COUNTS;
SELECT * FROM DEPT;
DECLARE
CURSOR c4 IS
SELECT dname, loc FROM DEPT FOR UPDATE OF loc;
    DEPT_rec c4%ROWTYPE;
    sales_count NUMBER := 0;
    non_sales NUMBER := 0;
BEGIN
    DBMS_OUTPUT.PUT_LINE('Q2.3:');
    OPEN c4;
    LOOP
        FETCH c4 INTO DEPT_rec;
        EXIT WHEN c4%NOTFOUND;
        IF DEPT_rec.dname = 'sales' AND DEPT_rec.loc != 'dallas' THEN
            UPDATE DEPT SET loc = 'dallas' WHERE CURRENT OF c4;
            sales_count := sales_count + 1;
        ELSE
            IF DEPT_rec.dname != 'sales' AND DEPT_rec.loc !=  'new york' THEN
                UPDATE DEPT SET loc = 'new york' WHERE CURRENT OF c4;
                non_sales := non_sales + 1;
            END IF;
        END IF;
    END LOOP;
    CLOSE c4;
    INSERT INTO COUNTS(sales_set, non_sales_set) VALUES(sales_count, non_sales);
    COMMIT;
END;
/
SELECT * FROM DEPT;
SELECT * FROM COUNTS;
DROP TABLE COUNTS;


CREATE USER scott IDENTIFIED by ubuntu;
GRANT DBA TO scott;
DISCONNECT;

CONN scott/ubuntu;
CREATE TABLE S_EMP AS (SELECT * FROM sys.EMP);
DESCRIBE S_EMP;

SET SERVEROUTPUT ON;
CREATE  OR REPLACE TRIGGER emp_hello
BEFORE DELETE OR INSERT OR UPDATE ON S_EMP
BEGIN
    --RAISE_APPLICATIO_ERROR(-20001, 'How are you!');
    DBMS_OUTPUT.PUT_LINE('How are you!');
END;
/

INSERT INTO S_EMP(empno, deptno) VALUES (9000, 10);
DELETE FROM S_EMP WHERE empno = 9000;

ALTER TRIGGER emp_hello DISABLE;
INSERT INTO S_EMP(empno, deptno) VALUES (9000, 10);
DELETE FROM S_EMP WHERE empno = 9000;

DROP TRIGGER emp_hello;

DISCONNECT;
CONN sys/ubuntu as sysdba;
DROP TABLE scott.S_EMP;
DROP USER scott;
