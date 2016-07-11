/* >> mysql -u root -p < ./form.sql */

DROP DATABASE IF EXISTS form;
CREATE DATABASE form CHARACTER SET 'utf8' COLLATE 'utf8_general_ci';
USE form;

CREATE TABLE Uploadcode (
    uploadcode VARCHAR(32) NOT NULL,
    PRIMARY KEY(uploadcode)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE Info (
    autokey INTEGER NOT NULL AUTO_INCREMENT,
    id VARCHAR(255) NOT NULL,
    password VARCHAR(32) NOT NULL,
    name VARCHAR(255) NOT NULL,
    cellphone VARCHAR(11) NOT NULL,
    email VARCHAR(255) NOT NULL,
    gender VARCHAR(8) DEFAULT 'Male',
    birthday VARCHAR(255) NOT NULL,
    birthplace VARCHAR(255) NOT NULL,
    info VARCHAR(1024),

    PRIMARY KEY(autokey),
    FOREIGN KEY(password) REFERENCES Uploadcode(uploadcode) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
