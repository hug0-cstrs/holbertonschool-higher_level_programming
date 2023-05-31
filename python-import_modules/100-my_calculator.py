#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys
    argc = len(sys.argv)
    if argc != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    ops = {'+': add, '-': sub, '*': mul, '/': div}
    operation = sys.argv[2]
    a = int(sys.argv[1])
    b = int(sys.argv[3])
    for i in ops:
        if i == operation:
            print("{} {} {} = {}".format(a, operation, b, ops[i](a, b)))
            break
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
