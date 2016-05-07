USE courseSelection;

DROP VIEW IF EXISTS S;
CREATE  VIEW S AS
SELECT
    id AS '学号',
    name AS '姓名',
    college_name AS '学院',
    passwd
FROM Students
ORDER BY 3, 1;

DROP VIEW IF EXISTS T;
CREATE VIEW T AS
SELECT
    id AS '工号',
    name AS '姓名',
    college_name AS '学院',
    passwd
FROM Teachers
ORDER BY 3, 1;

DROP VIEW IF EXISTS C;
CREATE VIEW C AS
SELECT
    id AS '课号',
    name AS '课程名',
    college_name AS '学院'
FROM Courses
ORDER BY 3, 1;

DROP VIEW IF EXISTS SC;
CREATE VIEW SC AS
SELECT
    semester,
    course_id,
    teacher_id,
    class_time,
    student_id,
    grade
FROM OpenCourses
ORDER BY 1, 2, 3, 4, 5
