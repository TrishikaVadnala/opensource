import math
import os
import random
import re
import sys

def plusMinus(arr):
    n = len(arr)
    positivecount = sum(1 for x in arr if x > 0)
    negativecount = sum(1 for x in arr if x < 0)
    zerocount = sum(1 for x in arr if x == 0)
    positiveratio = positivecount / n
    negativeratio = negativecount / n
    zeroratio = zerocount / n
    print(f"{positiveratio:.6f}")
    print(f"{negativeratio:.6f}")
    print(f"{zeroratio:.6f}")

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
