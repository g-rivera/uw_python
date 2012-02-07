# Guillermo Rivera
# UW Python 200 - Internet Programming in Python
# modified echo_www.py - echo_www_datetime.py

"""
hello_www.py - minimal web server + web application
"""

import socket 
import sys
from datetime import datetime

page = """
HTTP/1.0 200 OK
Content-Type text/html

<html>
<body>
Your URL request: %s
</body>
</html>
"""

datepage = """
HTTP/1.0 200 OK
Content-Type text/html

<html>
<body>
The current time is: %s
</body>
</html>
"""

host = '' 
port = 8082 # different default port than thirty_minute_webserver

# optional command line argument: port 
if len(sys.argv) > 1:
    port = int(sys.argv[1])

backlog = 5 
size = 1024 

# server's listener socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

# Release listener socket immediately when program exits, 
# avoid socket.error: [Errno 48] Address already in use
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

s.bind((host,port)) 

print 'hello_www listening on port', port
s.listen(backlog) 

while True: # just keep serving page to any client that connects
    client, address = s.accept() # create client socket
    request = client.recv(size).split() # HTTP request - split at spaces
    url = request[1] # set url as HTTP request URL
    if url == '/date.html': # set condition if url request is date.html
        client.send(datepage % datetime.now()) # send datepage
    else: client.send(page % url) # send page
    client.close()
