import sys
from collections import defaultdict
input = sys.stdin.readline

n = int(input())
rec = defaultdict(int)
answer = 0
for _ in range(n):
    a, b = map(int, input().split())
    
    if rec[a] == b:
        answer += 1
    
    rec[a] = b

for k, v in rec.items():
    if v == 1:
        answer += 1
print(answer)