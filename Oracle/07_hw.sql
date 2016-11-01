SYSTEM echo '对基本表S、C、SC进行操作：';
SYSTEM echo '1．用显式游标对基本表S查询信息。';
DECLARE CURSOR c1 IS
SELECT * FROM S;
v_sno VARCHAR2(8);
v_sname VARCHAR2(20);
v_age NUMBER(2);n
v_sex VARCHAR2(6);
BEGIN
    OPEN c1;
    FETCH c1 INTO v_sno, v_sname, v_age, v_sex;
    CLOSE c1;
END;

SYSTEM echo '2．用隐式游标对基本表C查询信息。';
DECLARE
v_cno VARCHAR2(8);
v_cname VARCHAR2(20);
v_teacher VARCHAR2(20);
BEGIN
   SELECT c#, cname, teacher INTO  v_cno, v_cname, v_teacher FROM C;
END;

SYSTEM echo '3．生成一个基本表S触发器，如果增加一个新的学生同时在基本表SC中也增加一条相同学号的记录。';
CREATE OR REPLACE TRIGGER t1
AFTER INSERT ON S
BEGIN
    INSERT INTO SC(s#) VALUES SC(NEW.s#);
END;

SYSTEM echo '4．生成一个基本表S触发器，如果删除一个学生时，同时也在基本表SC中删除所有该同学的课程成绩。';
CREATE OR REPLACE TRIGGER t2
AFTER DELETE ON S
BEGIN
    DELETE FROM SC WHERE SC.s# = OLD.s#;
END;

SYSTEM echo '5．删除生成的触发器。';
DROP TRIGGER t1;
DROP TRIGGER t2;
SYSTEM echo '1    SQL*PLUS';
SYSTEM echo '2    数据表的创建';
SYSTEM echo '3    数据插入、修改和删除';
SYSTEM echo '4    数据查询';
SYSTEM echo '5    视图、索引、序列和权限设置';
SYSTEM echo '6    PL/SQL（存储过程 函数 异常）';
SYSTEM echo '7    触发器和游标';
