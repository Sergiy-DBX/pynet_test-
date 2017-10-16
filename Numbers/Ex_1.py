#!/usr/bin/env python

from __future__ import print_function

try:
    number_one = raw_input("Enter Number one: ")
except NameError:
    number_one = input("Enter Number One: ")

try:
    number_two = raw_input("Enter Number two: ")
except NameError:
    number_two = input("Enter Number two: ")

print("Sum of Number One and Number Two is: {0}".format(int(number_one) + int(number_two)))
print("Difference of Number One and Number Two is: {0}".format(int(number_one) - int(number_two)))
print("Quotient of Number One and Number Two is: {0}".format(float(number_one)//float(number_two)))
print("Remainder of Number One and Number Two is: {0}".format(float(number_one) % float(number_two)))
