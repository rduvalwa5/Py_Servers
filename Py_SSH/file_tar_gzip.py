'''
Created on Nov 30, 2017
OS system calls
@author: rduvalwa2
'''

import os

def build_archive(path,fileName):
    tarCmd = "tar -cvf ./" + fileName + "  " + path
    print(tarCmd)
    os.system(tarCmd)
    compress = "gzip ./" + fileName
    os.system(compress)
    return fileName
    
    
    
if __name__ == '__main__':
    
    path = '"/Users/rduvalwa2/Music/iTunes/iTunes Music/Music/Zac Brown Band"'
    fileName = "zacBrown.tar"
    mytargzip = build_archive(path,fileName)
    os.system("ls -ltr")
