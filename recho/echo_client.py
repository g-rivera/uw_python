"""
echo client, usage:

 python echo_client.py <host> <port>

Both host and port are optional, defaults: localhost 50000
host must be present if you want to provide port
"""

import socket 
import sys

host = 'localhost' 
port = 50010 
size = 1024 

nargs = len(sys.argv)
if nargs > 1:
    host = sys.argv[1]
if nargs > 2:
    port = int(sys.argv[2])

prompt = raw_input('Enter a string to echo: ')
while len(prompt) > 0:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    s.connect((host,port)) 
    s.send(prompt) 
    data = s.recv(size)
    s.close()
    print 'from (%s,%s) %s' % (host, port, data)
    prompt = raw_input('Enter a string to echo: ')
