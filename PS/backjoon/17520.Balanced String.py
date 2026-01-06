import sys
import heapq, math
from collections import defaultdict, deque, Counter
input = sys.stdin.readline

n = int(input())

answer = 1 

for i in range((n+1)//2):
    answer *= 2
    answer %= 16769023
print(answer)