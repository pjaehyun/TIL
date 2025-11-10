import sys
import heapq
from collections import defaultdict, deque, Counter
input = sys.stdin.readline

n = int(input())

answer = 0
for _ in range(n):
    w = input().strip()

    stack = [w[0]]
    for i in range(1, len(w)):
        if not stack or stack[-1] != w[i]: 
            stack.append(w[i])
            continue

        while stack and stack[-1] == w[i]:
            stack.pop()
    
    if not stack:
        answer += 1
print(answer)