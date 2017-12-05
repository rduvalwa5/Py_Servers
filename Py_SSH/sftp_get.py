'''
https://gist.github.com/mlafeldt/841944
'''
import sys, paramiko

#if len(sys.argv) < 5:
#    print ("args missing")
#    sys.exit(1)

#hostname = sys.argv[1]
#password = sys.argv[2]
#source = sys.argv[3]
#dest = sys.argv[4]

hostname = 'Ubuntu_Osx'
password = 'blu4jazz'
username = 'rduvalwa2'
port = 22
source = '/Users/rduvalwa2/Public/oscAir_test_file.txt'
dest = '/Users/rduvalwa2/Server_Code/Py_Servers/Py_SSH/oscAir_test_file.txt'


username = "rduvalwa2"
port = 22



try:
    t = paramiko.Transport((hostname, port))
    print("opening connection to ", hostname , str(port) )
    t.connect(username=username, password=password)
    print("Getting ", source, "as ", dest)
    sftp = paramiko.SFTPClient.from_transport(t)
    sftp.get(source, dest)
#    sftp.get(dest, dest)
    
finally:
    print("closing connection to ", hostname)
    t.close()