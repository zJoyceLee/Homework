CREATE TABLE S (
  s# VARCHAR2(8) NOT NULL PRIMARY KEY,
  sname VARCHAR2(20),
  age NUMBER(2),
  sex VARCHAR2(6)
);

CREATE TABLE C (
  c# VARCHAR2(8) NOT NULL PRIMARY KEY,
  cname VARCHAR2(20),
  teacher VARCHAR2(20)
);

CREATE TABLE SC (
  s# VARCHAR2(8),
  c# VARCHAR2(8),
  grade NUMBER(3),
  PRIMARY KEY(s#, c#),
  FOREIGN KEY(s#) REFERENCES S(s#),
  FOREIGN KEY(c#) REFERENCES C(c#)
);

CREATE TABLE PROJECTS (
  projid NUMBER(4) NOT NULL PRIMARY KEY,
  p_desc VARCHAR2(20),
  p_start_date DATE,
  p_end_date DATE,
  budget_amount NUMBER(7, 2),
  max_no_staff NUMBER(2),
  CONSTRAINT check_date CHECK (p_start_date < p_end_date)
)

CREATE TABLE ASSIGNMENTS (
  projid NUMBER(4) NOT NULL,
  empno NUMBER(4) NOT NULL,
  a_start_date DATE,
  a_end_date DATE,
  bill_rate NUMBER(4, 2),
  assign_type VARCHAR2(2),
  FOREIGN KEY(projid) REFERENCES PROJECTS(projid),
  FOREIGN KEY(empno) REFERENCES EMP(empno)
)

DESCRIBE PROJECTS;
DESCRIBE ASSIGNMENTS;

ALTER TABLE PROJECTS ADD (comments LOB);
ALTER TABLE ASSIGNMENTS ADD (hours NUMBER);
