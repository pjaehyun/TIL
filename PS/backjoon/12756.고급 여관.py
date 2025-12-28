import sys
import heapq, math
from collections import defaultdict, deque, Counter
input = sys.stdin.readline

a1, l1 = map(int, input().split())
a2, l2 = map(int, input().split())

while True:
    
    if l1 <= 0 and l2 <= 0:
        print("DRAW")
        break
    elif l1 <= 0:
        print("PLAYER B")
        break
    elif l2 <= 0:
        print("PLAYER A")
        break
    l1 -= a2
    l2 -= a1