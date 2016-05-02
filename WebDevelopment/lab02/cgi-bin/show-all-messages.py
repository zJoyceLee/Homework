#!/usr/bin/python

import cgi, cgitb
import os
import json
# cgi.test()

print("Content-type: text/plain\r\n\r\n")
form = cgi.FieldStorage()
# print(form)

DB_FILE_PATH='/tmp/message-data.json'

data = ''
if not os.path.exists(DB_FILE_PATH):
    print('[]')
    exit(0)

with open(DB_FILE_PATH, 'r') as f:
    data = f.read()

if len(data) == 0:
  data = '[]'
print(data)
