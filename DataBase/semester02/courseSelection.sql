/*>>mysql -u root -p < courseSelection.sql */

DROP DATABASE IF EXISTS courseSelection;
CREATE DATABASE courseSelection CHARACTER SET 'utf8' COLLATE 'utf8_general_ci';
USE courseSelection;

CREATE TABLE Colleges (
    name VARCHAR(255) NOT NULL,

    PRIMARY KEY(name)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


CREATE TABLE Teachers (
    id CHAR(8) NOT NULL,
    name VARCHAR(255) NOT NULL,
    college_name VARCHAR(255) NOT NULL,
    passwd VARCHAR(20) NOT NULL,

    PRIMARY KEY(id),
    FOREIGN KEY(college_name) REFERENCES Colleges(name) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


CREATE TABLE Courses (
    id CHAR(8) NOT NULL,
    name VARCHAR(255) NOT NULL,
    college_name VARCHAR(255),

    PRIMARY KEY(id),
    FOREIGN KEY(college_name) REFERENCES Colleges(name) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


CREATE TABLE Students (
    id CHAR(8) NOT NULL,
    name VARCHAR(255) NOT NULL,
    college_name VARCHAR(255),
    passwd VARCHAR(20) NOT NULL,

    PRIMARY KEY(id),
    FOREIGN KEY(college_name) REFERENCES Colleges(name) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


CREATE TABLE OpenCourses (
    semester VARCHAR(255) NOT NULL,
    course_id CHAR(8) NOT NULL,
    teacher_id CHAR(8) NOT NULL,
    class_time VARCHAR(255) NOT NULL,
    rated INTEGER DEFAULT 50,
    num_of_student INTEGER DEFAULT 0,

    PRIMARY KEY(semester, course_id, teacher_id, class_time),
    FOREIGN KEY(course_id) REFERENCES Courses(id) ON DELETE CASCADE,
    FOREIGN KEY(teacher_id) REFERENCES Teachers(id) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE SC (
    sc_semester VARCHAR(255) NOT NULL,
    sc_course_id CHAR(8) NOT NULL,
    sc_teacher_id CHAR(8) NOT NULL,
    sc_class_time VARCHAR(255) NOT NULL,
    student_id CHAR(8) NOT NULL,
    grade INTEGER,

    PRIMARY KEY(sc_semester, sc_course_id, sc_teacher_id, sc_class_time, student_id),
    FOREIGN KEY(sc_semester, sc_course_id, sc_teacher_id, sc_class_time)
    REFERENCES OpenCourses(semester, course_id, teacher_id, class_time)
    ON DELETE CASCADE,
    FOREIGN KEY(student_id) REFERENCES Students(id) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

DELIMITER //
CREATE TRIGGER grade_trigger
BEFORE
UPDATE ON SC
FOR EACH ROW
BEGIN
    IF NEW.grade < 0 THEN
        SET NEW.grade = 0;
    ELSEIF NEW.grade > 100 THEN
        SET NEW.grade = 100;
    END IF;
END;//

CREATE INDEX student_grade ON SC (
    student_id ASC,
    sc_course_id ASC
);

/*
DELIMITER //
CREATE TRIGGER rated_trigger
BEFORE
INSERT ON SC
FOR EACH ROW
BEGIN
    IF
SELECT COUNT(student_id), SC.id, rated
FROM SC, OpenCourses
WHERE
    SC.id = OpenCourses.id
GROUP BY id;

    IF SC.grade < 0 THEN
        SET SC.grade = 0;
    ELSEIF SC.grade > 100 THEN
        SET SC.grade = 100;
    END IF;

END;//

DELIMITER;
*/
