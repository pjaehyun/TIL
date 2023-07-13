# 첫번째 풀이 완전탐색(Pypy3)
import sys

input = sys.stdin.readline

n, b, a = map(int, input().split())
gifts = list(map(int, input().split()))
gifts.sort()

answer = 0
_sum = 0

visited = [False] * n

for i in range(n):
    if _sum + gifts[i] <= b:
        _sum += gifts[i]
        answer += 1
    else:
        check = False
        for j in range(i, -1, -1):
            if a <= 0: break
            if visited[j]: continue

            _sum -= (gifts[j] // 2)
            visited[j] = True
            a -= 1

            if _sum + gifts[i] <= b:
                _sum += gifts[i]
                answer += 1
                check = True
                break
        if not check: break
print(answer)

# 두번째 풀이(누적합, 시간복잡도 개선)
import sys
from collections import deque

input = sys.stdin.readline

n, b, a = map(int, input().split())
gifts = list(map(int, input().split()))
gifts.sort()

answer = 0
c_sum = 0

for i in range(n):
    if i < a:
        c_sum += gifts[i] // 2
    else:
        c_sum += ((gifts[i-a] // 2) + (gifts[i] // 2))
    if c_sum <= b:
        answer += 1
print(answer)
