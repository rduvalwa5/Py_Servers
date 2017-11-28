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

hostname = 'c1246895-centos'
password = 'blu4jazz'
username = 'rduvalwa2'
port = 22
source = 'test_file.txt'
dest = 'oscAir_test_file.txt'



username = "rduvalwa2"
port = 22



try:
    t = paramiko.Transport((hostname, port))
    print("opening connection to ", hostname , str(port) )
    t.connect(username=username, password=password)
    print("Putting ", source, "as ", dest)
    sftp = paramiko.SFTPClient.from_transport(t)
    sftp.put(source, dest)
#    sftp.get(dest, dest)
    
finally:
    print("closing connection to ", hostname)
    t.close()