#!/usr/bin/env python3
for value in range(0, 99):
    print("{:02d}".format(value), end=", " if value < 98 else "")
