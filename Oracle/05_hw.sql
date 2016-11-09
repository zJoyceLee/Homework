CREATE VIEW maleStu AS
SELECT S.s#, sname, c#, grade FROM S, SC WHERE sex = 'M' AND S.s# = SC.s#;

SELECT s#, sname FROM maleStu
WHERE s# in (SELECT s# FROM  maleStu)
GROUP BY s#, sname HAVING AVG(grade) >  80;

DROP VIEW maleStu;

CREATE USER newuser IDENTIFIED BY helloworld;

GRANT SELECT, INSERT, DELETE, UPDATE ON S TO newuser;
GRANT SELECT, INSERT, DELETE, UPDATE ON C TO newuser;
GRANT SELECT, INSERT, DELETE, UPDATE ON SC TO newuser;

REVOKE ALL ON S FROM newuser;
REVOKE ALL ON C FROM newuser;
REVOKE ALL ON SC FROM newuser;

DROP USER newuser;

CREATE INDEX i_s# ON S(s#);
