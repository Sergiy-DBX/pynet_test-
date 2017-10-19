#!/usr/bin/env python

from getpass import getpass
from netmiko import ConnectHandler

def file_saver(device_name,output_txt):
    device_name_file = device_name + '.cfg'
    with open(device_name_file, 'wt') as new_file:
        new_file.write(output_txt)

pynet_rtr1 = {
    'device_type': 'cisco_ios',
    'ip':   '184.105.247.70',
    'username': 'pyclass',
    'password': getpass(),
}

srx = {
    'device_type': 'juniper_junos',
    'ip':   '184.105.247.76',
    'username': 'pyclass',
    'password': getpass(),
}

for device in (pynet_rtr1, srx):

    connector = ConnectHandler(**device)
    print(connector.find_prompt())
    print(connector.send_command("show version"))
    
    if device['device_type'] == 'juniper_junos':
        cur_config = connector.send_command("show config")
    else:
        cur_config = connector.send_command("show run")
     
    file_saver(device['device_type'], cur_config)

