from __future__ import print_function
import pdb

input_file = "../pynet-ons-oct17/day1/show_version.txt"

#pdb.set_trace()

with open(input_file) as input:
    for line in input:
        if "Processor board ID" in line:
            serial_number = line.split("ID")
            print(serial_number[1].strip())
            break
