# Oracle Database


## Environment
- Oracle Database Express Edition 11g Release 2: [Download Page](http://www.oracle.com/technetwork/database/database-technologies/express-edition/downloads/index.html)
- VirtualBox
- Ubuntu16.04 LTS

## Q&A
_How to start Oracle?_

    sudo service oracle-xe start
    sqlplus sys as sysdba

_How to run a script with sqlplus?_

    SQL> @ script.sql
    SQL> {START|@} {file}
