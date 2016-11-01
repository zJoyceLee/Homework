SYSTEM echo '1．声明显式游标';
SYSTEM echo '声明一个游标用来读取基表EMP中部门号是20且工作为分析员的职工：';
DECLARE CURSOR c1 IS
SELECT ename, sal, hiredate FROM EMP WHERE detpno = 20 AND  job = 'analyst';
v_name VARCHAR2(10);
v_sal NUMBER(7, 2);
v_hiredate DATE;
BEGIN
    OPEN c1;
    FETCH c1 INTO v_name, v_sal, v_hiredate;
    CLOSE c1;
END;

SYSTEM echo '2．游标的应用';
SYSTEM echo '使用游标属性判断游标是否打开：';
IF c1%OPEN THEN
    FETCH c1 INTO v_ename,  v_sal, v_hiredate;
ELSE
    OPEN c1;
END IF;
LOOP
    FETCH c1 INTO v_ename, v_sal, v_hiredate;
    EXIT WHEN c1%ROWCOUNT > 10;
END LOOP;

SYSTEM echo '利用游标修改数据，如果EMP中部门号是20，工作为分析员的职工工资小于2000，更改为2000：';
DECLARE CURSOR c2 IS
SELECT empno, sal, hiredate, rowid
FROM EMP WHERE deptno = 20 AND job = 'analyst'
FOR UPDATE OF sal;
EMP_record c2%ROWTYPE;
BEGIN
    OPEN c2;
    FETCH c2 INTO EMP_record;
    IF EMP_record.sal < 2000 THEN
        UPDATE EMP SET sal = 2000 WHERE empno = EMP_record.empno;
    END IF;
END;

SYSTEM echo '利用游标，如果部门是SALES，地址不是DALLAS的，地址更改为DALLAS；如果部门不是SALES，地址不是NEW YORK的，地址更改为NEW YORK：';
DECLARE CURSOR c3 IS
SELECT dname, loc FROM DEPT FOR UPDATE OF loc;
    DEPT_rec c3%ROWTYPE;
    sales_count NUMBER := 0;
    non_sales NUMBER := 0;
BEGIN
    OPEN c3;
    LOOP
        FETCH c3 INTO DEPT_rec;
        EXIT WHEN c3%NOTFOUND;
        IF DEPT_rec.dname = 'sales' AND DEPT_rec.loc != 'dallas' THEN
            UPDATE DEPT SET loc = 'dallas' WHERE CURRENT OF c3;
            sales_count := sales_count + 1;
        ELSE IF DEPT_rec.dname != 'sales' AND DEPT_rec.loc !=  'new yourk' THEN
            non_sales := non_sales + 1;
        END IF;
    END LOOP;
    CLOSE c3;
    INSERT INTO counts(sales_set, non_sales_set) VALUES(sales_count, non_sales);
    COMMIT;
END;

SYSTEM echo '3．创建触发器, 在SCOTT的EMP表上建立语句前触发器EMP_PERMIT_CHANGES。';
CREATE OR REPLACE TRIGGER scott.emp_hello
BEFORE
DELETE OR INSERT OR UPDATE
ON scott.EMP
BEGIN
    RAISE_APPLICATIO_ERROR(-20001, 'How are you!');
END;

SYSTEM echo '4．修改触发器, 使EMP_Hello触发器不能触发：';
ALTER TRIGGER scott.emp_hello DISABLE;

SYSTEM echo '5．删除触发器';
DROP TRIGGER scott.emp_hello;
