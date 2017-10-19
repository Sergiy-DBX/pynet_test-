#!/usr/bin/env python

import yaml
from pprint import pprint
from netmiko import ConnectHandler
from multiprocessing import Process

STREAM = '../../.netmiko.yml'

with open(STREAM) as file_in:
    devices = yaml.load(file_in)
pprint(devices)


def command_runner(gear):
    connector = ConnectHandler(**gear)
    print()
    print('*' * 40)
    print('*' * 40 )
    pprint(connector.find_prompt())
    print('-' * 40)
    print(connector.send_command("show version"))
#
for k,v in devices.items():
    #print(k,v)
    process = Process(target=command_runner, args=(v, ) )
    print(type(process))
    process.start()
#
