import sys
from collections import defaultdict, deque
input = sys.stdin.readline

n = int(input())



offset = [1, 2, 4, 7, 8, 11, 13, 14]

q = (n - 1) // 8         
r = (n - 1) % 8

print(q*15 + offset[r])
