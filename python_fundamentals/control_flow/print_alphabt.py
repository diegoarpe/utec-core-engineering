#!/usr/bin/env python3
for letter in range(ord("a"), ord("z") + 1):
    if letter == ord("e") or letter == ord("q"):
        continue
    else:
        print("{}".format(chr(letter)), end="\n" if letter == ord("z") else "")
