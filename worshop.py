#!/usr/bin/env python3

import math
import sys

def calculate(list):
    total = 0
    for i in list:
        total += i
    print(total)

def calc():
    for i in range(1,101):
        if (i % 3 == 0 and i % 5 != 0):
            print("Three")
        elif (i % 3 != 0 and i % 5 == 0):
            print("Five")
        elif (i % 3 == 0 and i % 5 == 0):
            print("ThreeFive")
        else:
            print(i)

def main():
    #calc()
    calculate([4, 3, -2])
main()