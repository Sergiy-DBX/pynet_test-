#!/usr/bin/env python

from __future__ import print_function
from pprint import pprint
from Ex1 import NetDevice

class NetDeviceAdd(NetDevice):
    
    def dev_printer(self):
        print("IP address: {}".format(self._ip_addr))

    def user_printer(self):
        print("Username: {}\nPassword: {}".format(self._username, self._password))

#def dev_printer(device_ip):
    
def main():
    #pass    
    device_1 = NetDeviceAdd('192.168.1.1', 'root', 'Passwd')
    print()
    device_1.dev_printer()
    print()
    device_1.user_printer()

    device_1.vendor='cisco'
    print(device_1.vendor)

if __name__ == '__main__':
    main()
