# Guillermo
# Python 200 - Internet Programming in Python
# wsgi-assignment

"""
Minimal WSGI + forms demo, with persistence

Send HTML page that echoes message from HTTP request,
also shows all messages received since startup.

To get started, point browser at echo_wsgi.html

Based on example in PEP 333, then add path and query processing
"""

import urlparse

# send one of these pages, depending on URL path

form_page = """<head>
<title>Echo request</title>
</head>
<body>
<form method="GET" action="echo_wsgi.py">
Message: <input type="text" name="message" size="40">
<input type="submit" value="Submit">
</form>
</body>
</html>
"""

message_template = """
<html>
<head>
<title>Echo response</title>
</head>
<body>
Message %s
<form>
<INPUT TYPE="button" VALUE="Back" onClick="history.go(-1);return true;">
</form>
</body>
</html>
"""

notfound_template = """
<html>
<head>
<title>404 Not Found</title>
</head>
<body>
404 %s not found
</form>
</body>
</html>
"""

# variable that stores a string with all of the messages submitted, newest first
posts = ""

# must be named 'application' to work with our wsgi simple server
def application(environ, start_response):
    global messages
    status = '200 OK'
    response_headers = [('Content_type', 'text/HTML')]
    start_response(status, response_headers)
    # send different page depending on URL path
    path = environ['PATH_INFO'] 
    if path == '/echo_wsgi.html':
        page = form_page
    elif path == '/echo_wsgi.py':
        # get message from URL query string, parse_qs returns a list for each key
        message = urlparse.parse_qs(environ['QUERY_STRING'])['message'][0]
        posts = ('%s<br>\n' % message) + posts # inserts html break at end of post
        page = message_template % post
    else:
        page = notfound_template % path
    return [ page ] # list of strings - must return iterable, not just a string
