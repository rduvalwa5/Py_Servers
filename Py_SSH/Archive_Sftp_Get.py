'''
https://gist.github.com/mlafeldt/841944
'''
import sys, paramiko
import os, glob, zipfile

class   archive_sftp():
    def __init__(self,archive_name, archive_path,host,uid,pwd ):
        self.filename = archive_name
        self.path = archive_path
        self.hostname = host
        self.username = uid
        self.password = pwd
    
    def restore_archive(self):
        fileName = self.filename
        tarCmd = "tar -xvzf /Users/rduvalwa2/Server_Code/Py_Servers/Py_SSH/" + fileName
        print(tarCmd)
        os.system(tarCmd)
        print("de compressed ", fileName)

    def  get_archive(self):
        hostname =  self.hostname  #'Ubuntu_Osx'
        password =  self.password  # 'blu4jazz'
        username =  self.username  #'rduvalwa2'
        port = 22
        source = self.filename
        print("get ",source)
        get_source = source  # + ".gz"
        print("source ",get_source)
        get_file = self.path + "/" + source # + ".gz"
        drop_file =  source
        print("drop file ",drop_file)
        try:
            t = paramiko.Transport((hostname, port))
            print("opening connection to ", hostname , str(port) )
            t.connect(username=username, password=password)
            print("Getting ", get_file, "as ", drop_file)
            sftp = paramiko.SFTPClient.from_transport(t)
            sftp.get(get_file,drop_file)   
        except Exception as e:
            print("Exception ", e)     
        finally:
            print("closing connection to ", hostname)
            t.close()
            
        print("restoring ", drop_file)
        self.restore_archive()

if __name__ == '__main__':
   
    host = 'Ubuntu_Osx'
    pwd =  'blu4jazz'
    uid =  'rduvalwa2'
    TarFile = 'OsxHosts.tar.gz'        # "OsxHosts2.tar.gz"
    archivePath = '/Users/rduvalwa2/Public'
    
    a = archive_sftp(TarFile,archivePath,host,uid,pwd)
    a.get_archive()
    os.system("ls -ltr | grep .gz")
    
#    a.send_archive(archv)