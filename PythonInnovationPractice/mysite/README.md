Form Generator
====
This project help to customize forms via Django1.9, Python3.4, SQLite.

Implement via django admin.

Process
----
Error like this:

    sqlite3.OperationalError: no such table: forms_form
    sqlite3.OperationalError: no such table: polls_question

Try this:

    python3 manage.py makemigrations yourapp
    python3 manage.py migrate
