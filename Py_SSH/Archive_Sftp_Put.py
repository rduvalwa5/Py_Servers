'''
    https://gist.github.com/mlafeldt/841944
    http://docs.paramiko.org/en/2.4/
    http://docs.paramiko.org/en/2.4/api/client.html

    Created on Nov 17, 2017
    https://pypi.python.org/pypi/scp
    https://pypi.python.org/pypi/scp
    /Library/Frameworks/Python.framework/Versions/3.6/bin

    Randalls-MBP-wired:bin rduvalwa2$ pip3.6 install scp
    Collecting scp
      Downloading scp-0.10.2-py2.py3-none-any.whl
    Collecting paramiko (from scp)
      Downloading paramiko-2.4.0-py2.py3-none-any.whl (192kB)
        100% |████████████████████████████████| 194kB 1.4MB/s 
    Collecting cryptography>=1.5 (from paramiko->scp)
    Downloading cryptography-2.1.3-cp36-cp36m-macosx_10_6_intel.whl (1.5MB)
        100% |████████████████████████████████| 1.5MB 428kB/s 
    Collecting pynacl>=1.0.1 (from paramiko->scp)
    Downloading PyNaCl-1.2.0-cp36-cp36m-macosx_10_6_intel.whl (243kB)
        100% |████████████████████████████████| 245kB 1.6MB/s 
    Collecting bcrypt>=3.1.3 (from paramiko->scp)
        Downloading bcrypt-3.1.4-cp36-cp36m-macosx_10_6_intel.whl (51kB)
        100% |████████████████████████████████| 61kB 4.1MB/s 
    Collecting pyasn1>=0.1.7 (from paramiko->scp)
        Downloading pyasn1-0.3.7-py2.py3-none-any.whl (63kB)
        100% |████████████████████████████████| 71kB 3.3MB/s 
    Collecting idna>=2.1 (from cryptography>=1.5->paramiko->scp)
        Downloading idna-2.6-py2.py3-none-any.whl (56kB)
        100% |████████████████████████████████| 61kB 2.7MB/s 
    Collecting asn1crypto>=0.21.0 (from cryptography>=1.5->paramiko->scp)
        Downloading asn1crypto-0.23.0-py2.py3-none-any.whl (99kB)
        100% |████████████████████████████████| 102kB 2.5MB/s 
    Collecting cffi>=1.7; platform_python_implementation != "PyPy" (from cryptography>=1.5->paramiko->scp)
        Downloading cffi-1.11.2-cp36-cp36m-macosx_10_6_intel.whl (240kB)
        100% |████████████████████████████████| 245kB 576kB/s 
    Collecting six>=1.4.1 (from cryptography>=1.5->paramiko->scp)
        Downloading six-1.11.0-py2.py3-none-any.whl
    Collecting pycparser (from cffi>=1.7; platform_python_implementation != "PyPy"->cryptography>=1.5->paramiko->scp)
        Downloading pycparser-2.18.tar.gz (245kB)
        100% |████████████████████████████████| 256kB 1.8MB/s 
    Installing collected packages: idna, asn1crypto, pycparser, cffi, six, cryptography, pynacl, bcrypt, pyasn1, paramiko, scp
        Running setup.py install for pycparser ... done
    Successfully installed asn1crypto-0.23.0 bcrypt-3.1.4 cffi-1.11.2 cryptography-2.1.3 idna-2.6 paramiko-2.4.0 pyasn1-0.3.7 pycparser-2.18 pynacl-1.2.0 scp-0.10.2 six-1.11.0

    Secure key information for Mac OSX
    /etc/ssh/ssh_host_key

    OSXAir:ssh rduvalwa2$ ls ~/.ssh
    github_rsa            github_rsa.pub_bak-github    known_hosts
    github_rsa.pub            github_rsa_bak-github

    OSXAir:.ssh rduvalwa2$ ls -ltr
    total 56
    -rw-------  1 rduvalwa2  staff  1766 Jun 25  2012 github_rsa_bak-github
    -rw-r--r--  1 rduvalwa2  staff   398 Jun 25  2012 github_rsa.pub_bak-github
    -rw-r--r--  1 rduvalwa2  staff   402 May  3  2015 github_rsa.pub
    -rw-------  1 rduvalwa2  staff  1766 May  3  2015 github_rsa
    -rw-r--r--  1 rduvalwa2  staff  9627 Nov 25 20:20 known_hosts
    OSXAir:.ssh rduvalwa2$ pwd
    /Users/rduvalwa2/.ssh

    scp syntax:   
    OSXAir:.ssh rduvalwa2$ scp ./testScpFile.txt rduvalwa2@c1246895-centos:~/testScpFile.txt
    rduvalwa2@c1246895-centos's password: 
    testScpFile.txt                                    100%   22     8.9KB/s   00:00    
    OSXAir:.ssh rduvalwa2$ 
    
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
        hostname =  self.hostname  #'Ubuntu_Osx'
        password =  self.password  # 'blu4jazz'
        username =  self.username  #'rduvalwa2'
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
   
    host = 'Ubuntu_Osx'
    pwd =  'blu4jazz'
    uid =  'rduvalwa2'
    TarFile = "OsxHosts2"
    archivePath = '/Users/rduvalwa2/hosts.txt'
    
    a = archive_sftp(TarFile,archivePath,host,uid,pwd)
    a.send_archive()
#    archv = a.build_archive(archivePath,TarFile)
#    print("output ", archv)
    os.system("ls -ltr | grep .gz")
    
#    a.send_archive(archv)