'''
https://docs.python.org/3/library/socketserver.html#module-socketserver
'''

import socket
import sys

class  client_example(object):
    def __init__(self,msg, hst, prt):
        self.message = msg
        self.host = hst
        self.port = prt
        
        
    def send_msg(self):
        print("In send")
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    # Connect to server and send data
            sock.connect((self.host,self.port))
            sock.sendall(bytes(self.message + "\n", "utf-8"))

    # Receive data from the server and shut down
            received = str(sock.recv(1024), "utf-8")
            print("Sent:     {}".format(msg))
            print("Received: {}".format(received))


if __name__ == '__main__':
    print("Start client")
    msg = 'The fat stupid developer thought highly of himself!'
    hst = 'localhost'
    prt = 9999
    
    clientSrv = client_example(msg, hst, prt)
    clientSrv.send_msg()



