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

    SQL> {START|@} [path] {file}

## Prepare

    SQL> @[path] prepare.sql

This file is used to do some prepare job. Contains: drop, create, insert.

First time run the script, you should use '--' to unable 'drop' command.
