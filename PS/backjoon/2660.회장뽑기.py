import sys
from collections import defaultdict, deque
input = sys.stdin.readline

n = int(input())

graph = defaultdict(list)

while True:
    a, b = map(int, input().split())

    if a == -1 and b == -1:
        break

    graph[a].append(b)
    graph[b].append(a)

def bfs(x):
    
    dq = deque()
    visited = [False] * (n+1)

    dq.append(x)
    visited[x] = True

    step = 0 
    while dq:
        for _ in range(len(dq)):
            curr = dq.popleft()

            for neib in graph[curr]:
                if not visited[neib]:
                    visited[neib] = True
                    dq.append(neib)
        step += 1
    return step - 1

pre = []
min_step = float('inf')
for i in range(1, n+1):
    step = bfs(i)
    pre.append((i, step))
    min_step = min(min_step, step)

answer = []

for i, step in pre:
    if step == min_step:
        answer.append(i)
print(min_step, len(answer))
print(*answer)