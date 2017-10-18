#!/usr/bin/env python

test_list = []
for i in range(1,6):
    test_list.append("String" + str(i))

#print(test_list)

test_list = test_list + ['Line add 1', 'Line add 2']

print(test_list)

test_list.pop(0)

print(test_list)

print(len(test_list))

test_list.sort()

print(test_list)    
