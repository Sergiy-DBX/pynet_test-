#!/usr/bin/env python

from __future__ import print_function
import re

show_file = '../../pynet-ons-oct17/day2/show_int_fa4.txt'

with open(show_file) as file_in:
    show_int = file_in.read()
    traffic_in = re.search('(\d+) packets input, (\d+) bytes', show_int)
    traffic_out = re.search('(\d+) packets output, (\d+) bytes,', show_int)
    #bps_in = re.search('(\d+) bytes', show_int)
    #bps_out = re.search('(\d+)  bytes,', show_int)
    print("Pps in: {}, Bps in: {}".format(traffic_in.group(1), traffic_in.group(2)))
    print("Pps out: {}, Bps out: {}".format(traffic_out.group(1), traffic_out.group(2)))
    #print(bps_in.group(1))
    #print(bps_out.group(1))

