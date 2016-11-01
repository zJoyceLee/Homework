SYSTEM echo '对基本表S、C和SC操作：';
SYSTEM echo '1．用PL/SQL的存储过程删除学号为S8的学生。';
DECLARE
BEGIN
    DELETE FROM S WHERE s# = 's8';
END;

SYSTEM echo '2．用带输入输出参数的存储过程查询出任意给定学号和课程后的成绩。';
CREATE OR REPLACE PROCEDURE query_grade (
    sno IN SC.s#%type,
    cno IN SC.c#%type,
    out_grade OUT SC.grade%type
) IS
BEGIN
    SELECT grade FROM SC WHERE s# = sno AND c# = cno;
END query_grade;
VARIABLE sc_grade NUMBER(3);
EXECUTE query_grade('s1', 'c1', :out_grade);
PRINT out_grade;

SYSTEM echo '3．用函数做第2题。';
CREATE OR REPLACE FUNCTION Fun_query_grade (
    sno IN SC.s#%type,
    cno IN SC.c#%type
) RETURN NUMBER
IS
    val_grade SC.grade%type := 0;
BEGIN
    SELECT grade INTO val_grade FROM SC WHERE s# = sno AND c# = cno;
    RETURN (val_grade);
END Fun_query_grade;
VARIABLE sc_grade NUMBER(3);
EXECUTE :sc_grade := Fun_query_grade('s1', 'c1');
PRINT sc_grade;
