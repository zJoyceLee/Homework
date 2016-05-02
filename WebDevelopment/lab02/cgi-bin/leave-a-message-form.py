#!/usr/bin/python

import cgi, cgitb
import os
import json
# cgi.test()

print("Content-type: text/plain\r\n\r\n")
form = cgi.FieldStorage()
# print(form)

form_keys = form.keys()
try:
    [form_keys.index(field) for field in ['name', 'email', 'gender', 'hobby', 'messageArea']]
except ValueError as e:
    print('Invalid Data')
    exit(0)

DB_FILE_PATH='/tmp/message-data.json'

data = ''
if not os.path.exists(DB_FILE_PATH):
    fd = os.open(DB_FILE_PATH, os.O_RDWR | os.O_CREAT)
    os.close(fd)
else:
    with open(DB_FILE_PATH, 'r') as f:
        data = f.read()

if len(data) == 0:
  data = '[]'
data = json.loads(data)
data.append({
    'name': form['name'].value,
    'email': form['email'].value,
    'gender': form['gender'].value,
    'hobby': form.getlist('hobby'),
    'messageArea': form['messageArea'].value
})
print(json.dumps(data))
with open(DB_FILE_PATH, 'w') as f:
    f.write(json.dumps(data))

