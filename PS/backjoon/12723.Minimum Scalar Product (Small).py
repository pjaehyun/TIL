import sys
import heapq, math
from collections import defaultdict, deque, Counter
input = sys.stdin.readline

t = int(input())

for X in range(t):
    n = int(input())
    v1 = sorted(list(map(int, input().split())))
    v2 = sorted(list(map(int, input().split())), reverse=True)

    vsum = 0

    for i in range(n):
        vsum += (v1[i] * v2[i])
    
    print("Case #{}: {}".format(X+1, vsum))