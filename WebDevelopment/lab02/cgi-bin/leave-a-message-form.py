import cgi, cgitb

# form = cgi.FieldStorage()

# first_name = form.getvalue('first_name')
# last_name = form.getvalue('last_name')

print("Content-tpye:text/html\r\n\r\n")
print("<html>")
print("<head>")
print("<title>Hello - Second CGI Program</title>")
print("</head>")
print("<body>")
# print("<Hello {0} {1}".format(first_name, last_name))
print("<h1>CGI Script Output</h2>")
print("</body>")
print("</html>")
