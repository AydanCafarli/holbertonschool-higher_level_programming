#!/usr/bin/python3
"""
0-add.py - Imports a simple function from a simple file.
This script assigns values to variables a and b, then prints
the result of adding them using a function from add_0.py.
"""


if __name__ == "__main__":
    from add_0 import add

    a = 1
    b = 2
    print("{} + {} = {}".format(a, b, add(a, b)))
