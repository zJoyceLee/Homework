DataBase
============

How to install MySQL on Ubuntu:

    sudo apt install mysql-server

* [install instruction](https://help.ubuntu.com/lts/serverguide/mysql.html)

How to use MySQL in Python:

    import MySQLdb

If there show 'ImportError: No module named MySQLdb':

    pip install MySQL-python

Or you are using python3:

     pip3 install mysqlclient

You can connect db like this:

    import MySQLdb
    db = MySQLdb.connect('localhost', user, passwd, dbName, charset='utf8')
    cursor = db.cursor()

Pay attention to:

     try:
         # execute
         db.commit()
     except:
         db.rollback()

How to write Trigger in MySQL:

    DELIMITER //
    create trigger [trigger_name]
    [before/after]
    [insert/delete/update] on [table_name]
    for each row
    begin
        --doing something like this
        insert into tab2(tab2_id) values (new.tab1_id);
    end;//

    DELIMITER;

I wrote a trigger in mysql command line like this:

table is SC:

    CREATE TABLE SC (
        id CHAR(10) NOT NULL,
        student_id CHAR(8),
        grade INTEGER,

        PRIMARY KEY(id, student_id),
        FOREIGN KEY(id) REFERENCES OpenCourses(id) ON DELETE CASCADE,
        FOREIGN KEY(student_id) REFERENCES Students(id) ON DELETE CASCADE
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8;

trigger like this:

    DELIMITER //
    CREATE TRIGGER grade_trigger
    BEFORE
    INSERT ON SC
    FOR EACH ROW
    BEGIN
        IF NEW.grade < 0 THEN
            SET NEW.grade = 0;
        ELSEIF NEW.grade > 100 THEN
            SET NEW.grade = 100;
        END IF;
    END;//

Pay attention to table name:

* INSERT: NEW
* DELETE: OLD
* UPDATE: NEW and OLD
