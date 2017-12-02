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
    return fileName



hostname = 'ubuntu_osx'
password = 'blu4jazz'
username = 'rduvalwa2'
port = 22
TarFile = "ZacBrownArchive"
archivePath = '"/Users/rduvalwa2/Music/iTunes/iTunes Music/Music/Zac Brown Band"'
#archiveFile.zip = create_archive(zipPath)
source = build_archive(archivePath,TarFile)
#print("result is", source)
send_source = "./" + source + ".gz"
print("source ",send_source)
dest_file = source + ".gz"
dest = '/home/rduvalwa2/Public/Music/' + dest_file
print("dest ",dest)
username = "rduvalwa2"
port = 22
os.system("ls -ltr")

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
