DROP DATABASE IF EXISTS webLab;
CREATE DATABASE webLab CHARCTER SET 'utf8' COLLATE 'utf8_general_ci';
USE webLab;

CREATE TABLE info (
    userName VARCHAR(255) NOT NULL,
    passwd VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    question
    anwser VARCHAR(255) NOT NULL,

    PRIMARY KEY userName
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
