from collections import defaultdict, deque

N, M = map(int, input().split())

graph = defaultdict(set)
visited = set()

dq = deque()
dq.append((N, 0))
visited.add(N)

while dq:
    cur, d = dq.popleft()

    if cur == M:
        print(d)
        break
    for _next in [cur+1, cur-1, cur*2]:
        if 0 <= _next <= 100000 and _next not in visited:
            dq.append((_next, d+1))
            visited.add(_next)
