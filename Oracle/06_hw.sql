INSERT INTO S(s#, sname, age, sex) VALUES ('s8', 'dong', 18, 'F');
SELECT s#, sname FROM S WHERE s# = 's8';
CREATE OR REPLACE PROCEDURE delStu (val IN S.s#%type)
IS
BEGIN
    DELETE FROM S WHERE s# = val;
END delStu;
/
EXECUTE delStu('s8');
SELECT s#, sname FROM S WHERE s# = 's8';


SELECT * FROM SC;
CREATE OR REPLACE PROCEDURE query_grade (
    sno IN SC.s#%type,
    cno IN SC.c#%type,
    out_grade OUT SC.grade%type
) IS
BEGIN
    SELECT grade INTO out_grade FROM SC WHERE s# = sno AND c# = cno;
END query_grade;
/
VARIABLE sc_grade NUMBER;
EXECUTE query_grade('s1', 'c1', :sc_grade);
PRINT sc_grade;

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
/
VARIABLE f_sc_grade NUMBER;
EXECUTE :f_sc_grade := Fun_query_grade('s1', 'c1');
PRINT f_sc_grade;
