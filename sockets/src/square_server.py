'''
Created on Jun 3, 2016

@author: rduvalwa2
'''

from socket import * # get socket constructor and constants
myHost = '' # '' = all available interfaces on host
myPort = 50001 # listen on a non-reserved port number
sockobj = socket(AF_INET, SOCK_STREAM) # make a TCP socket object
sockobj.bind((myHost, myPort)) # bind it to server port number
sockobj.listen(5) # listen, allow 5 pending connects

while True: # listen until process killed
    print("server started on %", myPort)
    connection, address = sockobj.accept() # wait for next client connect
    print('Server connected by', address) # connection is a new socket
    while True:
        data = connection.recv(1024) # read next line on client socket      
        if not data: break # send a reply line to the client
        print("Server Got" , data)
        result = int(data) * int(data)
        print(result)
        sendThis = str(result)
        print(sendThis)
        convB = bin(result)
        connection.send(convB) # until eof when socket closed
    connection.close()