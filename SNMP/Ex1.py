#!/usr/bin/env python

from __future__ import print_function, unicode_literals
import getpass
import snmp_helper

def main():

    try:
        ip_addr_1 = raw_input("Router 1 IP: ")
        ip_addr_2 = raw_input("Router 2 IP: ")
    except NameError:
        ip_addr_1 = input("Router 1 IP: ")
        ip_addr_2 = input("Router 2 IP: ")


    snmpv3_key = getpass(prompt="SNMP v3 key: ")
#Connect to the router
#SNMP authentication
#Send OID
#Get MIB data
#Interprit data
#Return data
    
if __name__ == '__main__':
    main()
