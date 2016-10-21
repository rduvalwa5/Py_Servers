'''
example of socket.getaddrinfo
lsof - list open files
OSXAir:GitRepos rduvalwa2$ lsof | grep 3306
MySQLWork 32138 rduvalwa2   15u     REG               1,4    143360 27506390 /Users/rduvalwa2/Library/Application Support/MySQL/Workbench/cache/Local_instance_3306.cache
MySQLWork 32138 rduvalwa2   16u     REG               1,4     12288 12397367 /Users/rduvalwa2/Library/Application Support/MySQL/Workbench/cache/Local_instance_3306.column_widths
MySQLWork 32138 rduvalwa2   18w     REG               1,4         6 27506410 /Users/rduvalwa2/Library/Application Support/MySQL/Workbench/sql_workspaces/Local_instance_3306-1.autosave/lock

'''
import socket

class  get_socket:
    def __init__(self,host, port):
        self.host = host
        self.port = port
#        self.proto = proto#proto=socket.IPPROTO_TCP
    def printInput(self):
        print(self.host, self.port)
        
    def get_info(self):
        print('get address for port ', self.port)
        result = 'not right'
        try:
            result = socket.getaddrinfo(self.host, self.port,proto=socket.IPPROTO_TCP)
            return result
        except Exception as err:
            print("Error ",  err) 
    
    def get_fqd_name(self):
        '''
        socket.getfqdn([name])
        '''
        return  socket.getfqdn(self.host) 
     
    def get_host_Byname(self,name):
        '''
        socket.gethostbyname(hostname)
        '''
        self.name = name
        return  socket.gethostbyname(self.name)
    
    def get_host_ByName_ex(self,hostname):
        '''
        socket.gethostbyname_ex(hostname)
      '''
        return  socket.gethostbyname_ex(hostname)
    
 
    def get_hostName(self):
        '''
        socket.gethostname()
        '''
        return  socket.gethostname()

    def get_host_byIP(self,ip_address):
        '''
        socket.gethostbyaddr(ip_address)¶
        '''
        return  socket.gethostbyaddr(ip_address)
    
    def get_nameInfo(self,sockaddr,flags):
        '''
        socket.getnameinfo(sockaddr, flags)
        https://developer.apple.com/library/ios/documentation/NetworkingInternet/Conceptual/NetworkingTopics/Articles/UsingSocketsandSocketStreams.html
        https://developer.apple.com/library/ios/documentation/System/Conceptual/ManPages_iPhoneOS/man3/getnameinfo.3.html

    Scan Ports on an IP or Domain from Mac OS X
    1) Hit Command+Spacebar to summon Spotlight and type “Network Utility” followed by the return key to launch 
       the Network Utility app.
    2) Select the “Port Scan” tab.
    3) Enter the IP or domain name you wish to scan for open ports and choose “scan”
    Port Scanning host: 127.0.0.1

Port Scanning host: 127.0.0.1

     Open TCP Port:     22             ssh
     Open TCP Port:     80             http
     Open TCP Port:     88             kerberos
     Open TCP Port:     445            microsoft-ds
     Open TCP Port:     548            afpovertcp
     Open TCP Port:     631            ipp
     Open TCP Port:     3031           eppc
     Open TCP Port:     3306           mysql
     Open TCP Port:     5900           rfb
     Open TCP Port:     8080           http-alt
     Open TCP Port:     49158
     Open TCP Port:     49161
     Open TCP Port:     57107
Port Scan has completed…

    [22,80,88,445,548,631,3031,3306,3370,5900,8080,49175]
    '''
        return socket.getnameinfo(sockaddr, flags)
    
'''
socket.getnameinfo(sockaddr, flags)
Translate a socket address sockaddr into a 2-tuple (host, port). Depending on the settings of flags, the result can contain a fully-qualified domain name or numeric address representation in host. Similarly, port can contain a string port name or a numeric port number.

socket.getprotobyname(protocolname)
Translate an Internet protocol name (for example, 'icmp') to a constant suitable for passing as the (optional) third argument to the socket() function. This is usually only needed for sockets opened in “raw” mode (SOCK_RAW); for the normal socket modes, the correct protocol is chosen automatically if the protocol is omitted or zero.

socket.getservbyname(servicename[, protocolname])
Translate an Internet service name and protocol name to a port number for that service. The optional protocol name, if given, should be 'tcp' or 'udp', otherwise any protocol will match.

socket.getservbyport(port[, protocolname])
Translate an Internet port number and protocol name to a service name for that service. The optional protocol name, if given, should be 'tcp' or 'udp', otherwise any protocol will match.

'''
    
if __name__ == '__main__':
    # "example.org", 80, proto=socket.IPPROTO_TCP
    host = "192.168.1.3" # "example.org" # 'localhost'
    port = 3306  # 80 # '3306'
    #   proto = 'proto=socket.IPPROTO_TCP'
    mySocket = get_socket(host,port)
    mySocket.printInput()
    result = mySocket.get_info()
    print("the result ",result)
    print("OSXAir ",mySocket.get_fqd_name())
    print("OSXAir by name ", mySocket.get_host_Byname("osxair.home.home"))
    print("OSXAir by name expanded", mySocket.get_host_ByName_ex("osxair.home.home"))
    myEmpty = get_socket("",port)
    print("empty ", myEmpty.get_fqd_name())
    print("empty host by name ", myEmpty.get_host_Byname(""))
    myXPS = get_socket("192.168.1.8",22)
    print("XPS ", myXPS.get_fqd_name())
    print("XPS info",  myXPS.get_info())
    print("XPS by name ", myXPS.get_host_Byname('c1246895-xps'))    
    myNonExist = get_socket("192.168.1.108",22)
    print("myNonExist ", myNonExist.get_fqd_name())
    print("myNonExist info",  myNonExist.get_info()) 
    
    try: 
        print("myNonExist by name ", myNonExist.get_host_Byname('fakeName')) 
    except Exception as error:
        print(error)
        
    print("Python running on ",mySocket.get_hostName())
    print("host by id ", mySocket.get_host_byIP('192.168.1.3'))
    print("host by id",mySocket.get_host_byIP('192.168.1.20'))
    flags = [0,1,2,3]
    # ports = [3306,22,80,21,8080,2048,50787]
    ports = [21,22,80,88,445,548,631,3031,3306,3370,5900,8080,49175]
    for flag in flags:
        print('flag ', flag)
        for port in ports:
            print('getname info on service on ' + str(port) , mySocket.get_nameInfo(('192.168.1.3',port),flag))
'''
0
getname info ('osxair.home.home', 'mysql')
getname info ('osxair.home.home', 'ssh')
getname info ('osxair.home.home', 'http')
getname info ('osxair.home.home', 'ftp')
1
getname info ('osxair.home.home', 'mysql')
getname info ('osxair.home.home', 'ssh')
getname info ('osxair.home.home', 'http')
getname info ('osxair.home.home', 'ftp')
2
getname info ('192.168.1.3', 'mysql')
getname info ('192.168.1.3', 'ssh')
getname info ('192.168.1.3', 'http')
getname info ('192.168.1.3', 'ftp')
3
getname info ('192.168.1.3', 'mysql')
getname info ('192.168.1.3', 'ssh')
getname info ('192.168.1.3', 'http')
getname info ('192.168.1.3', 'ftp')

    '''