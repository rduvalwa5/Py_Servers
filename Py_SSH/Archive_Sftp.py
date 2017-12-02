'''
https://gist.github.com/mlafeldt/841944
'''
import sys, paramiko
import os, glob, zipfile

class   archive_sftp():
    def __init__(self,archive_name, archive_path ):
        self.filename = archive_name
        self.path = archive_path
    
    def build_archive(self):
        fileName = self.filename + ".tar"
        tarCmd = "tar -cvf ./" + fileName + "  " + self.path
        print(tarCmd)
        os.system(tarCmd)
        compress = "gzip ./" + fileName
        print("compress command ", compress)
        os.system(compress)
        print("compressed ", fileName)
        return fileName + ".gz"

    def  send_archive(self):
        hostname = 'Ubuntu_Osx'
        password = 'blu4jazz'
        username = 'rduvalwa2'
        port = 22
#    TarFile = "ZacBrownArchive"
#    archivePath = '"/Users/rduvalwa2/Music/iTunes/iTunes Music/Music/Zac Brown Band"'
        source = self.build_archive()
        print("send ",source)
        send_source = "./" + source  # + ".gz"
        send_source = source  # + ".gz"
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
   
    TarFile = "OsxHosts"
    archivePath = '/Users/rduvalwa2/hosts.txt'
    a = archive_sftp(TarFile,archivePath)
    a.send_archive()
#    archv = a.build_archive(archivePath,TarFile)
#    print("output ", archv)
    os.system("ls -ltr | grep .gz")
    
#    a.send_archive(archv)