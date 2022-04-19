#!/usr/bin/env python3

import math
import sys

def calc():
    i = 1
    for i in range(0, 101):
        if (i % 3 == 0 and i % 5 != 0):
            print("Three")
        elif (i % 3 != 0 and i % 5 == 0):
            print("Five")
        elif (i % 3 == 0 and i % 5 == 0):
            print("ThreeFive")
        else:
            print(i)

def main():
    calc()
main()