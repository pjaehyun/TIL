import sys
from collections import defaultdict, deque

input = sys.stdin.readline

N, M = map(int, input().split())

ladder =  defaultdict(int)
dice = [1,2,3,4,5,6]

for _ in range(N+M):
    s, e = map(int, input().split())
    ladder[s] = e


def bfs():
    visited = [False] * 101
    dq = deque()

    dq.append((1, 0))
    visited[1] = True

    while dq:
        s, count = dq.popleft()

        if s == 100:
            return count

        for num in dice:
            ds = s + num
            if ds <= 100 and not visited[ds]:
                visited[ds] = True
                if ds in ladder:
                    ds = ladder[ds]
                    visited[ds] = True
                dq.append((ds, count+1))

print(bfs())