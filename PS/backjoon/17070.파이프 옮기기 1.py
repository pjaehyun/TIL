# 첫번째 풀이(DFS, Pypy3)
import sys
input = sys.stdin.readline

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

graph[0][0], graph[0][1] = 1, 1
answer = 0
def dfs(x, y, direction):
    global answer
    if x == n-1 and y == n-1:
        answer += 1
        return
    if direction == "h" or direction == "d":
        xx, yy = x, y+1
        if 0 <= xx < n and 0 <= yy < n and graph[xx][yy] == 0:
            dfs(xx, yy, "h")
    if direction == "v" or direction == "d":
        xx, yy = x+1, y
        if 0 <= xx < n and 0 <= yy < n and graph[xx][yy] == 0:
            dfs(xx, yy, "v")
    if 0 <= x+1 < n and 0 <= y+1 < n and graph[x+1][y] == 0 and graph[x][y+1] == 0 and graph[x+1][y+1] == 0:
        dfs(x+1, y+1, "d")
dfs(0, 1, "h")
print(answer)

# 두번째 풀이(DP)
import sys
input = sys.stdin.readline

n = int(input())

graph = [list(map(int, input().split())) for _ in range(n)]
dp = [[[0] * n for _ in range(n)] for _ in range(3)]

dp[0][0][1] = 1

for i in range(2, n):
    if graph[0][i] == 0:
        dp[0][0][i] = dp[0][0][i-1]

for r in range(1, n):
    for c in range(1, n):
        if graph[r][c] == 0 and graph[r][c-1] == 0 and graph[r-1][c] == 0:
            dp[2][r][c] = dp[0][r-1][c-1] + dp[1][r-1][c-1] + dp[2][r-1][c-1]
        
        if graph[r][c] == 0:
            dp[0][r][c] = dp[0][r][c-1] + dp[2][r][c-1]
            dp[1][r][c] = dp[1][r-1][c] + dp[2][r-1][c]
print(sum(dp[i][n-1][n-1] for i in range(3)))