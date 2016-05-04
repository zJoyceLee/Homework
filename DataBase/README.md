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
    create trigger [trigger_name] [before/after] [insert/delete/update] on [table_name] for each row
    begin
        --doing something like this
        insert into tab2(tab2_id) values (new.tab1_id);
    end;//

    DELIMITER;



