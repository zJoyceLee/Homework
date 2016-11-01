INSERT INTO CUSTOMERS VALUES ('Nicholson', 'CA', 6989.99);
INSERT INTO CUSTOMERS VALUES ('Martin', 'CA', 2345.45);
INSERT INTO CUSTOMERS VALUES ('Laursen', 'CA', 34.34);
INSERT INTO CUSTOMERS VALUES ('Bambi', 'CA', 1234.55);
INSERT INTO CUSTOMERS VALUES ('McGraw', 'NJ', 123.45);

INSERT INTO STATE(state_name, state_cd) VALUES ('Massachusetts', 'MA');
INSERT INTO STATE(state_name, state_cd) VALUES ('California', 'CA');
INSERT INTO STATE(state_name, state_cd) VALUES ('NewJersey', 'NJ');
INSERT INTO STATE(state_name, state_cd) VALUES ('New York', 'NY');

UPDATE STATE SET state_name = 'Florida', state_id = 'FD'
WHERE state_name = 'New York' AND state_id = 'NY';

DELETE FROM STATE WHERE state_name = 'Florida' AND state_cd = 'FD';
