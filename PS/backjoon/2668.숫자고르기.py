import sys
input = sys.stdin.readline

n = int(input())

graph = {1:0 for _ in range(1, n+1)}

for i in range(n):
    num = int(input())
    graph[i+1] = num

def dfs(x, foot, par):
    global count
    if not visited[graph[x]]:
        visited[graph[x]] = True
        dfs(graph[x], foot + [graph[x]], par)
    else:
        if graph[x] == par:
            for f in foot:
                if not is_cycle[f]:
                    count += 1
                    is_cycle[f] = True

is_cycle = [False] * (n+1)
count = 0

for i in range(1, n+1):
    visited = [False] * (n+1)
    if not visited[i]:
        visited[i] = True
        dfs(i, [i], i)

print(count)
for i in range(n+1):
    if is_cycle[i]:
        print(i)