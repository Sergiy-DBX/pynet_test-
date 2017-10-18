#!/usr/bin/env python

ip_address_block = '192.168.10.'
ip_list = []
for i in range(128):
    ip_list.append(ip_address_block + str(i))

#print(ip_list)

ip_addr = ip_list[-1].split('.')

#print(ip_addr)

ip_addr[-1] = int(0)

#print(ip_addr)

print("{0}, {1}, {2}, {3}".format(*ip_addr))

d_one = ip_addr[0]
d_two = ip_addr[1]
d_three = ip_addr[2]
d_four = ip_addr[3]

print("Digit one: {0}, Digit two: {1}, Digit three: {2}, Digit four: {3}".format(bin(int(d_one)), bin(int(d_two)), bin(int(d_three)), bin(int(d_four))))
