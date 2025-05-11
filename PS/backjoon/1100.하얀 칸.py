import sys
input = sys.stdin.readline

def dfs(x, y, curr):
    for nx, ny in [(x+1,y),(x,y+1),(x-1,y),(x,y-1)]:
        if 0<=nx<8 and 0<=ny<8 and chess[nx][ny] == -1:
            v = curr^1
            chess[nx][ny] = v
            dfs(nx, ny, v)

status = list(input().strip() for _ in range(8))

chess = [[-1] * 8 for _ in range(8)]

chess[0][0] = 0
dfs(0, 0, 0)

answer = 0
for i in range(8):
    for j in range(8):
        if chess[i][j] == 0 and status[i][j] == "F":
            answer += 1

print(answer)