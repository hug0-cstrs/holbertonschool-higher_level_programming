#!/usr/bin/python3
for ch in reversed(range(97, 123)):
    if ch % 2 == 0:
        print("{:c}".format(ch), end='')
    else:
        print("{:c}".format(ch - 32), end='')
