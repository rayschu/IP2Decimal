#!/usr/bin/env python
import sys

def IP2Decimal(IP): 
    IP1 = IP.split('.')[0]
    IP2 = IP.split('.')[1]
    IP3 = IP.split('.')[2]
    IP4 = IP.split('.')[3]
    IP_Dec = int(IP1)*256**3 + int(IP2)*256**2 + int(IP3)*256 + int(IP4)
    print("Your IP is: %s" % IP)
    print ("Your Decimal IP is: %d" % IP_Dec)
IP2Decimal(sys.argv[1])
