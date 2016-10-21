'''
Created on Sep 11, 2016

@author: rduvalwa2
'''

import socket

 

class verify_servers(object):
    '''
    classdocs
    '''
    def __init__(self, servers = ['localhost']):
        '''
        Constructor
        '        '''
        self.servers = servers
    
    def get_local_hostName(self):
        '''
        socket.gethostname()
        '''
        local_server = socket.gethostname()
        return   local_server
                
    def get_server_(self):
        serverData = []
        for server in self.servers:
            if server[0:2].isdigit() and server[3] == '.': 
#                print("input is ip address ", server)
                serverData.append(self.get_host_byIP(server))
                
            else:
#                print("input is hostname ", server) 
                serverData.append(self.get_host_ByName_ex(server)) 
        return serverData
    
    
    def get_hostName(self,name):
        '''
        socket.gethostname()
        '''
        return  socket.gethostname(name)
    
    def get_host_ByName_ex(self,hostname):
        '''
        socket.gethostbyname_ex(hostname)
      '''
        return  socket.gethostbyname_ex(hostname)

    def get_host_byIP(self,ip_address):
        '''
        socket.gethostbyaddr(ip_address)¶
        '''
        return  socket.gethostbyaddr(ip_address)  
    

'''
finish this class
'''
class verify_server_ports(object):
    '''
    classdocs
    '''
    def __init__(self, servers, ports_list, flags):
        '''
        Constructor
        '''
        self.ports = ports_list
        self.servers = servers 
        self.flags = flags
        
    def print_input(self):
        print(self.servers)   
        print(self.ports)
        print(self.flags)
        
    def verify_server_ports_(self):
        '''
        flags = [0,1,2,3]
        ports = [21,22,80,88,445,548,631,3031,3306,3370,5900,8080,49175]
        for flag in flags:
                print('flag ', flag)
            for port in ports:
                    print('getname info on service on ' + str(port) , mySocket.get_nameInfo(('192.168.1.3',port),flag))
        '''
        serverPortData = []
        self.flags = flags
        for server in self.servers:
            for flag in self.flags:
                for port in self.ports:
#                    print('server ', server, 'port ', port)
                    serverPortData.append(socket.getnameinfo((server,port), flag))
#                    print('S',serverPortData)
            
        return serverPortData
    

if __name__ == '__main__':
    
    hosts = ['localhost','192.168.1.3','195FakeName.com']
#    ipHosts = ['192.168.1.17','50.47.25.136','192.168.1.3','192.168.1.20','192.168.1.11']
#    ipHosts = ['50.47.25.136','192.168.1.1']
    ipHosts = ['192.168.1.111']
    isHostname = verify_servers(hosts)
    flags = [0,1,2,3]
#    ports = [21,22,80,88,445,548,631,3031,3306,3370,5900,8080,49175]
    ports = [22,23,80,88,443,445,548,631,992,2555,2556,3031,3306,3689,4567,5900,7020,8023,8080,8443,49158,49161,49400,55087,59549]
#    for p in range(0,50000):
#        ports.append(p)
    local_server = isHostname.get_local_hostName()
    print("get_local_hostName() is", local_server)
    
    for item in isHostname.get_server_():
        print(type(item) , item)

    hostPorts = verify_server_ports(ipHosts,ports,flags)
    hostPorts.print_input()
    output =  hostPorts.verify_server_ports_()
    for result in output:
        print(type(result) ,result)
    
'''
Port Scan has started…

Port Scanning host: 50.47.25.136

     Open TCP Port:     23             telnet
     Open TCP Port:     80             http
     Open TCP Port:     443            https
     Open TCP Port:     992            telnets
     Open TCP Port:     2555           compaq-wcp
     Open TCP Port:     2556           nicetec-nmsvc
     Open TCP Port:     4567           tram
     Open TCP Port:     7020           dpserve
     Open TCP Port:     8023
     Open TCP Port:     8080           http-alt
     Open TCP Port:     8443           pcsync-https
Port Scan has completed…

Port Scan has started…

Port Scanning host: 192.168.1.1

     Open TCP Port:     23             telnet
     Open TCP Port:     80             http
     Open TCP Port:     443            https
     Open TCP Port:     992            telnets
     Open TCP Port:     2555           compaq-wcp
     Open TCP Port:     2556           nicetec-nmsvc
     Open TCP Port:     4567           tram
     Open TCP Port:     7020           dpserve
     Open TCP Port:     8023
     Open TCP Port:     8080           http-alt
     Open TCP Port:     8443           pcsync-https
Port Scan has completed…

Port Scan has started…

Port Scanning host: 192.168.1.20

     Open TCP Port:     22             ssh
Port Scan has completed…

Port Scan has started…
Port Scanning host: 192.168.1.17

     Open TCP Port:     22             ssh
     Open TCP Port:     80             http
     Open TCP Port:     88             kerberos
     Open TCP Port:     445            microsoft-ds
     Open TCP Port:     631            ipp
     Open TCP Port:     5900           rfb
Port Scan has completed…

Port Scan has started…

Port Scanning host: 192.168.1.3

     Open TCP Port:     22             ssh
     Open TCP Port:     80             http
     Open TCP Port:     88             kerberos
     Open TCP Port:     445            microsoft-ds
     Open TCP Port:     548            afpovertcp
     Open TCP Port:     3031           eppc
     Open TCP Port:     3306           mysql
     Open TCP Port:     3689           daap
     Open TCP Port:     5900           rfb
     Open TCP Port:     8080           http-alt
     Open TCP Port:     49158
     Open TCP Port:     49161
     Open TCP Port:     49400
     Open TCP Port:     55087
     Open TCP Port:     59549
Port Scan has completed…

22,23,80,88,443,445,548,631,992,2555,2556,3031,3306,3689,4567,5900,7020,8023,8080,8443,49158,49161,49400,55087,59549
'''
    