#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
from sys import argv, exit, stderr


def main():
    if len(argv) != 4:
        stderr.write("Usage: ./100-my_calculator.py <a> <operator> <b>\n")
        exit(1)

    a = int(argv[1])
    b = int(argv[3])
    operator = argv[2]
    operators = ['+', '-', '*', '/']
    operation = [add, sub, mul, div]

    if operator not in operators:
        stderr.write("Unknown operator. Available operators: +, -, * and /\n")
        exit(1)

    for i in range(4):
        if operator == operators[i]:
            print("{} {} {} = {}".format(a, operator, b, operation[i](a, b)))

    exit(0)


if __name__ == "__main__":
    main()
