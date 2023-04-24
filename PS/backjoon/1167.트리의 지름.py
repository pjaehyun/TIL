import sys
from collections import defaultdict

input = sys.stdin.readline

N = int(input())

tree = defaultdict(list)

for _ in range(N):
    temp = list(map(int, input().split()))
    for i in range(1, len(temp), 2):
        if temp[i] != -1:
            tree[temp[0]].append((temp[i], temp[i+1]))

def dfs(node):
    for neib, dist in tree[node]:
        if distance[neib] == -1:
            distance[neib] = distance[node] + dist
            dfs(neib)
    

distance = [-1] * (N+1)
distance[1] = 0
dfs(1)

start = distance.index(max(distance))
distance = [-1] * (N+1)
distance[start] = 0
dfs(start)
print(max(distance))
