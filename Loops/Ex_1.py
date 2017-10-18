#!/usr/bin/env python

ord_numbers = []
for i in range(1,50):
    ord_numbers.append(i)

print(ord_numbers)

for j in ord_numbers:
    if j == 13:
        continue
    elif j > 39:
        break
    else:
        print(j)
