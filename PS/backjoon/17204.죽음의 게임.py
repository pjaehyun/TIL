import sys
input = sys.stdin.readline

n, k = map(int, input().split())

graph = {x:int(input()) for x in range(n)}

visited = [False] * n

def dfs(x, count):
    global answer
    if x == k:
        answer = count
        return
    if not visited[graph[x]]:
        visited[graph[x]] = True
        dfs(graph[x], count + 1)

visited[0] = True
answer = -1
dfs(0, 0)
print(answer)