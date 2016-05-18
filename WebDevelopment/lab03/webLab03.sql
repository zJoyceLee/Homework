DROP DATABASE IF EXISTS webLab03;
CREATE DATABASE webLab03 CHARACTER SET 'utf8' COLLATE 'utf8_general_ci';
USE webLab03;

CREATE TABLE User (
    username VARCHAR(255) NOT NULL,
    passwd VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    birthday VARCHAR(255) NOT NULL,
    birthplace VARCHAR(255) NOT NULL,
    gender VARCHAR(8) DEFAULT 'Male',
    hobby VARCHAR(255) NOT NULL,
    info VARCHAR(1024),
    photo_path VARCHAR(1024),

    PRIMARY KEY(username)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
