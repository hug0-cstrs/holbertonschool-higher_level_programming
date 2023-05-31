#!/usr/bin/python3
if __name__ == "__main__":
    import sys

i = len(sys.argv) - 1

if i == 0:
    print("{:d} arguments.".format(i))
elif i == 1:
    print("{:d} argument:".format(i))
else:
    print("{:d} arguments:".format(i))

if i >= 1:
    i = 0
    for arg in sys.argv:
        if i != 0:
            print("{:d}: {:s}".format(i, arg))
        i += 1
