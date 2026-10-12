#!/usr/bin/env python3
for left in range(10):
    for right in range(left + 1, 10):
        last = (left == 10 - 2 and right == 10 - 1)
        print("{:01d}{:01d}".format(left,right), end="\n" if last else ", ")
