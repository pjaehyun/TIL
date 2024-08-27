import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

N, M = map(int, input().split())

_set = set()
answer = 0

for _ in range(N):
    _set.add(input().strip())

for _ in range(M):
    word = input().strip()
    if word in _set:
        answer += 1
print(answer)