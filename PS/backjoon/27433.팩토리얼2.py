import sys
import heapq, math
from collections import defaultdict, deque, Counter
input = sys.stdin.readline


n = int(input())

def fac(n):
    res = 1
    for i in range(1, n+1):
        res *= i
    return res

print(fac(n))