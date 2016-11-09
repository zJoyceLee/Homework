SET SERVEROUTPUT ON;

DECLARE
    CURSOR c1 IS
    SELECT * FROM S;
v_sno S.s#%TYPE;
v_sname S.sname%TYPE;
v_age S.age%TYPE;
v_sex S.sex%TYPE;
BEGIN
    DBMS_OUTPUT.PUT_LINE('Q1．用显式游标对基本表S查询信息。');
    OPEN c1;
    FETCH c1 INTO v_sno, v_sname, v_age, v_sex;
    DBMS_OUTPUT.PUT_LINE(
        'sno: ' || v_sno ||
        ', sname: ' || v_sname ||
        ', age: ' || v_age ||
        ', gender: ' || v_sex);
    CLOSE c1;
END;
/


BEGIN
    DBMS_OUTPUT.PUT_LINE('2．用隐式游标对基本表C查询信息。');
    FOR c_rec in (SELECT c#, cname, teacher FROM C)
    LOOP
          DBMS_OUTPUT.PUT_LINE(
            'cno: ' || c_rec.c# ||
            ', cname: ' || c_rec.cname  ||
            ', teacher: ' || c_rec.teacher);
    END LOOP;
END;
/


CREATE USER scott IDENTIFIED BY ubuntu;
GRANT DBA TO scott;
DISCONNECT;

CONN scott/ubuntu;
SET SERVEROUTPUT ON;

CREATE TABLE S_S AS (SELECT * FROM sys.S);
DESCRIBE S_S;
CREATE TABLE S_SC AS (SELECT * FROM sys.SC);
DESCRIBE S_SC;

CREATE OR REPLACE TRIGGER t1
AFTER INSERT ON S_S
FOR EACH ROW
BEGIN
    DBMS_OUTPUT.PUT_LINE('3．生成一个基本表S触发器，如果增加一个新的学生同时在基本表SC中也增加一条相同学号的记录。');
    INSERT INTO S_SC(s#) VALUES (:NEW.s#);
END;
/
SELECT * FROM S_SC WHERE s# = 's99';
INSERT  INTO S_S VALUES ('s99', 'Joyce', 22, 'Female');
show errors;
SELECT * FROM S_SC WHERE s# = 's99';

CREATE OR REPLACE TRIGGER t2
AFTER DELETE ON S_S
FOR EACH ROW
BEGIN
    DBMS_OUTPUT.PUT_LINE('4 ．生成一个基本表S触发器，如果删除一个学生时，同时也在基本表SC中删除所有该同学的课程成绩。');
    DELETE FROM S_SC WHERE S_SC.s# = :OLD.s#;
END;
/
SELECT * FROM S_SC WHERE s# = 's1';
DELETE FROM S_S WHERE s# = 's1';
SELECT * FROM S_SC WHERE s# = 's1';

DROP TRIGGER t1;
DROP TRIGGER t2;
DROP TABLE S_S;
DROP TABLE S_SC;
DISCONNECT;
CONN sys/ubuntu as sysdba;
DROP USER scott CASCADE;
