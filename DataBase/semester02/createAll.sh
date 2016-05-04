#! /bin/sh

echo "Creating  Database courseSelection now ..."
# create Database: courseSelection
mysql -u root -p1 < ./courseSelection.sql

echo "Insert data now ..."
# insert into Colleges, Students, Teachers, Courses
echo "This spend time totle: "
time python ./insert.py

echo "Create View now ..."
# createView: S, T, C
mysql -u root -p1 < ./createView.sql
