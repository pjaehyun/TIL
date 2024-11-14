import sys
input = sys.stdin.readline

def dfs(x, y, step):
    global answer
    if (x, y) == (0, c-1) and step == k:
        answer += 1
        return
    for nx, ny in [(x+1,y),(x,y+1),(x-1,y),(x,y-1)]:
        if 0<=nx<r and 0<=ny<c and not visited[nx][ny] and graph[nx][ny] != 'T':
            visited[nx][ny] = True
            dfs(nx, ny, step+1)
            visited[nx][ny] = False

r, c, k = map(int, input().split())
graph = [input().strip() for _ in range(r)]
visited = [[False] * c for _ in range(r)]
visited[r-1][0] = True
answer = 0
dfs(r-1, 0, 1)
print(answer)