#!/usr/bin/env python

import yaml
from pprint import pprint
from netmiko import ConnectHandler
from multiprocessing import Process,Queue
import pdb

STREAM = '../../.netmiko.yml'

with open(STREAM) as file_in:
    devices = yaml.load(file_in)
#pprint(devices)


def command_runner(gear):
    output = {}
    connector = ConnectHandler(**gear)
    #print()
    output_header = '\n' + '*' * 40 + '\n'
    hostname = connector.find_prompt()
    output_footer = '\n' + '*' * 40 + '\n'
    output_value = connector.send_command("show version")
    output[hostname] = output_header + output_value + output_footer
    process_queue.put(output)
#pdb.set_trace()

process_queue = Queue(maxsize = 50)

procs = []
for k,v in devices.items():
    #print(k,v)
    process = Process(target=command_runner, args=(v, ) )
    print(type(process))
    process.start()
    procs.append(process)

for proc in procs:
    proc.join()

while not process_queue.empty():
    output_dict = process_queue.get()
    for i,j in output_dict.items():
        print("Hostname: {}".format(i))
        print("{}".format(j))
        print()
        print()
        print()
