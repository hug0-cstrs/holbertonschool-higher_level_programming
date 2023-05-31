#!/usr/bin/python3
if __name__ == "__main__":
    import sys
i = len(sys.argv) - 1

result = 0
for arg in sys.argv:
    if arg != sys.argv[0]:
        result += int(arg)
print(result)
