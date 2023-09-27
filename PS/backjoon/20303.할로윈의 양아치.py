import sys
from collections import defaultdict, deque
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

def bfs(x):
    dq = deque()
    dq.append(x)
    visited[x] = True
    group = [candies[x], 1]
    
    while dq:
        curr = dq.popleft()
        for neib in kids[curr]:
            if not visited[neib]:
                group[0] += candies[neib]
                group[1] += 1
                visited[neib] = True
                dq.append(neib)
    return group

n, m, k = map(int, input().split())
candies = [0] + list(map(int, input().split()))
kids = defaultdict(list)
candy_group = []

for _ in range(m):
    a, b = map(int, input().split())
    kids[a].append(b)
    kids[b].append(a)

visited = [False] * (n + 1)
for i in range(1, n+1):
    if not visited[i]:
        candy_group.append(bfs(i))

dp = [[0] * (k + 1) for _ in range(len(candy_group)+1)]
for i in range(1, len(candy_group)+1):
    for j in range(1, k+1):
        if j >= candy_group[i-1][1]:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-candy_group[i-1][1]] + candy_group[i-1][0])
        else:
            dp[i][j] = dp[i-1][j]
print(dp[-1][k-1])