#!/usr/bin/env python

from __future__ import print_function

str_one = "10.10.10.0"
str_two = "10.10.20.0"
str_three = "10.10.30.0"

try:
    str_four = raw_input("Enter IP Address: ")
except NameError:
    str_four = input("Enter IP Address: ")

print("{0:>20s} {1:^20s} {2:<20s}".format(str_one, str_two, str_three))
print("{:>10}".format(str_four))
    
