import sys
sys.setrecursionlimit(1000000)

N = int(input())

tree = [[] for _ in range(N + 1)]
parent = [-1] * (N+1)

for i in range(N - 1):
    n1, n2 = map(int, input().split())
    tree[n1].append(n2)
    tree[n2].append(n1)

def dfs(n):
    for i in tree[n]:
        if parent[i] == -1:
            parent[i] = n
            dfs(i)
dfs(1)

for i in range(2, len(parent)):
    print(parent[i])