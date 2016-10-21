'''
Created on Sep 15, 2016

https://docs.python.org/3/library/socketserver.html#module-socketserver
'''
 
import socketserver

class MyTCPHandler(socketserver.BaseRequestHandler):
    """
    The request handler class for our server.

    It is instantiated once per connection to the server, and must
    override the handle() method to implement communication to the
    client.
    """

    def handle(self):
        # self.request is the TCP socket connected to the client
        self.data = self.request.recv(1024).strip()
        print("Handler {} wrote:".format(self.client_address[0]))
        print(self.data)
        # just send back the same data, but upper-cased
        self.request.sendall(self.data.upper())

'''    `                                                                                                                                                                                                                                                                                
    An alternative request handler class that makes use of streams (file-like objects that simplify 
    communication by providing the standard file interface):
'''
class MyTCPHandler2(socketserver.StreamRequestHandler):

    def handle(self):
        # self.rfile is a file-like object created by the handler;
        # we can now use e.g. readline() instead of raw recv() calls
        self.data = self.rfile.readline().strip()
        print("Handle2 {} wrote:".format(self.client_address[0]))
        print(self.data)
        # Likewise, self.wfile is a file-like object used to write back
        # to the client
        self.wfile.write(self.data.upper())



if __name__ == "__main__":
    
    HOST = "localhost"
    PORT =  9999
    PORT2 = 9998
    
    # Create the server, binding to localhost on port 9999
    server = socketserver.TCPServer((HOST, PORT), MyTCPHandler)
 #   server2 = socketserver.TCPServer((HOST, PORT2), MyTCPHandler2)

    # Activate the server; this will keep running until you
    # interrupt the program with Ctrl-C
    server.serve_forever()       
 #   server2.serve_forever(poll_interval = 1)