"""Simple command-line calculator."""

import argparse
import operator

OPERATIONS = {
    'add': operator.add,
    'sub': operator.sub,
    'mul': operator.mul,
    'div': operator.truediv,
}

def calculate(op, a, b):
    if op not in OPERATIONS:
        raise ValueError(f"Unsupported operation: {op}")
    return OPERATIONS[op](a, b)

def main():
    parser = argparse.ArgumentParser(description="Run a simple calculator")
    parser.add_argument('operation', choices=OPERATIONS.keys(), help='Operation to perform')
    parser.add_argument('a', type=float, help='First operand')
    parser.add_argument('b', type=float, help='Second operand')
    args = parser.parse_args()
    result = calculate(args.operation, args.a, args.b)
    print(result)

if __name__ == '__main__':
    main()
