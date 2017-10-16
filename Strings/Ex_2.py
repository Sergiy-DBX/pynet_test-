#!/usr/bin/env python

from __future__ import print_function

try:
    ip_input = raw_input("Enter IP address: ")
except NameError:
    ip_input = input("Enter IP address: ")

digits = ip_input.split('.')
for i in digits:
    print("{:>12}".format(i))
