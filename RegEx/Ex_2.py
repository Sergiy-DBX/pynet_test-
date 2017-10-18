#!/usr/bin/env python

from __future__ import print_function
import re
import json

show_file = '../../pynet-ons-oct17/day2/show_mac_multicast.txt'

with open(show_file) as file_in:
    show_input = file_in.read()
    
    #print(show_input)

    arp_record = re.search('(\d+?)\s.*?(\w+.\w+.\w+.\w+)\s.*?(\w+)\s.*?(.+)', show_input)
    #print(arp_record) 
    #print(arp_record.group(0))
    
    int_dict = {'vlan':arp_record.group(1), 'type':arp_record.group(3), 'ports':arp_record.group(4).split(',')}
    arp_dict = {}
    arp_dict[arp_record.group(2)] = int_dict
    print(arp_dict)
    print()
    print(json.dumps(arp_dict, indent=4))
