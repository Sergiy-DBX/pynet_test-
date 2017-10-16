#!/usr/bin/env python

from __future__ import print_function

with open("../File_example.txt") as file_in:
    for line in file_in:
        print(line.strip())

print('#' * 40)

file_to_write = open("../File_example.txt", "wt")
print(file_to_write)
file_to_write.write("Line one\nLine two\nLine three\n")
file_to_write.flush()
file_to_write.close()

print('#' * 40)

append_file = open("../File_example.txt", "at")
append_file.write("Line Three and Half\n")
append_file.flush()

append_file.seek(0)
append_file.write("Line addition\n")
append_file.flush()
append_file.close()

print(append_file)

file_read = open("../File_example.txt")
print(file_read.read())
