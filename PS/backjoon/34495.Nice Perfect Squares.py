import sys
import heapq, math
from collections import defaultdict, deque, Counter
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    
    if n == 4:
        print("2025")
    elif n == 5:
        print("42025")
    elif n % 2 == 0:
        print("2025" + "0"*(n-4))
    else:
        print("1092025" + "0"*(n-7))