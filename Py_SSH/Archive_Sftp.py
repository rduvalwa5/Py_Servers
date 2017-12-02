'''
https://gist.github.com/mlafeldt/841944
'''
import sys, paramiko
import os, glob, zipfile

def build_archive(path,fileName):
    fileName = fileName + ".tar"
    tarCmd = "tar -cvf ./" + fileName + "  " + path
    print(tarCmd)
    os.system(tarCmd)
    compress = "gzip ./" + fileName
    print("compress command ", compress)
    os.system(compress)
    print("compressed ", fileName)
    return fileName + ".gz"

def  send_archive(source):
    hostname = 'ubuntu_osx'
    password = 'blu4jazz'
    username = 'rduvalwa2'
    port = 22
#    TarFile = "ZacBrownArchive"
#    archivePath = '"/Users/rduvalwa2/Music/iTunes/iTunes Music/Music/Zac Brown Band"'
#    source = build_archive(archivePath,TarFile)
    send_source = "./" + source  # + ".gz"
    print("source ",send_source)
    dest_file = source # + ".gz"
    dest = '/home/rduvalwa2/Public/' + dest_file
    print("dest ",dest)

    try:
        t = paramiko.Transport((hostname, port))
        print("opening connection to ", hostname , str(port) )
        t.connect(username=username, password=password)
        print("Putting ", send_source, "as ", dest)
        sftp = paramiko.SFTPClient.from_transport(t)
        print("sending ", send_source ,"as ", dest)
        sftp.put(send_source, dest)
        
    finally:
        print("closing connection to ", hostname)
        t.close()

if __name__ == '__main__':
    TarFile = "ZacBrownArchive"
    archivePath = '"/Users/rduvalwa2/Music/iTunes/iTunes Music/Music/Zac Brown Band/Greatest Hits So Far"'

    a = build_archive(archivePath,TarFile)
    print("output ", a)
    os.system("ls -ltr | grep .gz")
    
    send_archive(a)