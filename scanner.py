#!/bin/python3

import sys # allows us to enter command line args
import socket
from datetime import datetime

# define the target

if len(sys.argv) == 2:
    target = socket.gethostbyname(sys.argv[1])
else:
    print("Invalid Args")
    print("Syntax: python3 scanner.py <ip/hostname>")
    sys.exit()

# Add a pretty banner

print("-" * 50)
print("Scanning target " + target)
print("Time Started: "+str(datetime.now()))
print("-" * 50)

try:
    for port in range(50, 85):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = s.connect_ex((target,port))
        print("Checking port {}".format(port))
        if result == 0:
            print("Port {} is open".format(port))
        s.close()

except KeyboardInterrupt:
        print("\nExiting Program.")
        sys.exit()

except socket.gaierror:
        print("Hostname could not be resolved.")
        sys.exit()

except socket.error:
        print("Couldn't connect to server.")
        sys.exit()