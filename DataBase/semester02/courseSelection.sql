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
    FOREIGN KEY(college_name) REFERENCES Colleges(name)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


CREATE TABLE Courses (
    id CHAR(8) NOT NULL,
    name VARCHAR(255) NOT NULL,
    college_name VARCHAR(255),

    PRIMARY KEY(id),
    FOREIGN KEY(college_name) REFERENCES Colleges(name)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


CREATE TABLE Students (
    id CHAR(8) NOT NULL,
    name VARCHAR(255) NOT NULL,
    college_name VARCHAR(255),
    passwd VARCHAR(20) NOT NULL,

    PRIMARY KEY(id),
    FOREIGN KEY(college_name) REFERENCES Colleges(name)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE OpenCourses (
    semester VARCHAR(255) NOT NULL,
    course_id CHAR(8) NOT NULL,
    teacher_id CHAR(8) NOT NULL,
    class_time VARCHAR(255),
    rated INTEGER,

    PRIMARY KEY(course_id, teacher_id, semester, class_time),
    FOREIGN KEY(course_id) REFERENCES Courses(id),
    FOREIGN KEY(teacher_id) REFERENCES Teachers(id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
