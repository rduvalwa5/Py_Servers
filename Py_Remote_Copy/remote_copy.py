'''
Created on Nov 17, 2017

https://kb.froglogic.com/display/KB/Example+-+Copying+files+to+remote+computer+with+Python+2.6+%28or+higher%29
'''
import subprocess
import sys
import multiprocessing.managers

host = "127.0.0.1"
port = 8989
password = "Secret"
commands = ["echo %USERPROFILE%", "dir \\", "echo $HOME", "ls /", "non_existing_command"]

def write_file(file_name, file_contents):
    fh = None
    try:
        fh = open(file_name, "wb")
        fh.write(file_contents)
        return True
    except:
        return False
    finally:
        if fh is not None:
            fh.close()

class RemoteManager(multiprocessing.managers.BaseManager):
    pass

RemoteManager.register("write_file", write_file)

def start_server(port, password):
    print ("Listening for incoming connections...")
    mgr = RemoteManager(address=('', port), authkey=password)
    server = mgr.get_server()
    server.serve_forever()

def write_file_remote(host, port, password, file_name_remote, file_contents):
    mgr = RemoteManager(address=(host, port), authkey=password)
    mgr.connect()
    print (mgr.write_file(file_name_remote, file_contents)._getvalue())
    print ("\n")

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--server":
        start_server(port, password)
    elif len(sys.argv) > 3 and sys.argv[1] == "--client":
        fh = None
        try:
            fh = open(sys.argv[2], "rb")
            file_contents = fh.read()
        finally:
            if fh is not None:
                fh.close()
        file_name_remote = sys.argv[3]
        write_file_remote(host, port, password, file_name_remote, file_contents)
    else:
        print ("usage: python " + sys.argv[0] + " [ --server | --client <local_file_name> <remote_file_name>]" )