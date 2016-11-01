SYSTEM echo '对基本表S、C和SC操作'
SYSTEM echo '1．建立男学生的视图，属性包括学号、姓名、选修课程和成绩。';
CREATE VIEW maleStu AS
SELECT s#, sname, c#, grade FROM S, SC WHERE sex = 'M' AND S.s# = SC.s#;

SYSTEM echo '2．在男学生视图中查询平均成绩大于80分的学生学号和姓名。';
SELECT s#, sname FROM maleStu WHERE AVG(grade) >  80 GROUP BY s#;

SYSTEM echo '3．撤消生成的视图。';
DROP VIEW maleStu;

SYSTEM echo '4．创建一个新用户NEWUSER。';
CREATE USER newuser IDENTIFIED BY helloworld;

SYSTEM echo '5．使用GRANT语句，把对基本表S、C、SC的使用权限授给NEWUSER用户。';
GRANT SELECT, INSERT, DELETE, UPDATE ON S TO newuser;
GRANT SELECT, INSERT, DELETE, UPDATE ON C TO newuser;
GRANT SELECT, INSERT, DELETE, UPDATE ON SC TO newuser;

SYSTEM echo '6．使用REVOKE语句从NEWUSER手中收回基本表S、C、SC的使用权。';
REVOKE ALL ON S FROM newuser;
REVOKE ALL ON C FROM newuser;
REVOKE ALL ON SC FROM newuser;

SYSTEM echo '7．删除用户NEWUSER。';
DROP USER newuser;

SYSTEM echo '8．对基本表S按照S#生成一个索引。';
--CREATE INDEX i_s# ON S(s#);
SYSTEM echo '9．对基本表C按照C#生成一个索引。';
SYSTEM echo '10．删除基本表C建立的索引。';
