#!/usr/bin/python

import socket
import sys, time
from datetime import datetime
import code


#declare program settings
host = ''
max_port = 500000
min_port = 1

def scan_host(host,port,r_code = 1):
    try:
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        code = s.connect_ex(host,port)
        if code== 0:
            r_code = code
        s.close()
    except Exception:
        pass
    return r_code
    
#initiate program test for interrupt
try:
        host = input("[*] Enter Target Host Address: ")
except  KeyboardInterrupt:
            print("\n\n[*] User Interrupt.")
            print("[*] Application Shut Down")
            sys.exit(1)
            
hostip = socket.gethostbyname(host)
print("\n[*] Host: %s IP: %s"  % (host,  hostip))
print("[*] Scanning Started At %s...\n" % (time.strftime("%H:%M:%S")))
start_time = datetime.now()
    
for port in range(min_port, max_port):
        try:
            response = scan_host(host, port)
            if response == 0:
                print("[*] Port %d: Open" % (port))
#            else:
#                print("Port Not Open: ", port)
        except Exception:
            pass
        
stop_time = datetime.now()
total_time_duration = stop_time - start_time
print("\n[*] Scanning Finished At %s ..." % (time.strftime("%H:%M:%S")))
print("\n[*] Scanning Duration: %s ..." % (total_time_duration))
print("\n] Good Bye World")
