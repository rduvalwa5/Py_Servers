'''
Created on Jun 3, 2016

@author: rduvalwa2
'''

import sys
from socket import *  # portable socket interface plus constants
serverHost = 'localhost'   # server name or 'starship.python.net'
serverPort  = 50001

#m = bin(2)
#print("M is" , m)
num = b'2'

#message = [m_string]      # default text to send to server
                                        # requires bytes: b'' or str, encode()
if len(sys.argv) > 1:
    serverHost = sys.argv[1]            # server from cmd lione arg 1
    if len(sys.argv) > 2:               # test from cmd line args 2...n
        message = (x.encode() for x in sys.argv[2:])
        
sockobj = socket(AF_INET, SOCK_STREAM)     # make a TCP?IP soclet object
sockobj.connect((serverHost, serverPort))   # conect to server

sockobj.send(num)              # send line to server
data = sockobj.recv(1024)       # receive line from server up to 1k
print('Client recieved:', data)
    
sockobj.close()