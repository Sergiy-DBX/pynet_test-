#!/usr/bin/env python

import yaml

STREAM = '../../.netmiko.yml'

with open(STREAM) as file_in:
    devices = yaml.load(file_in)
print(devices)


