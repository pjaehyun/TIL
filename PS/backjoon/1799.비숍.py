# 일반적인 백트래킹으로 풀었으나 시간초과
# 고민하다 해법을 못찾아 다른 풀이 참고
import sys
input = sys.stdin.readline

n = int(input())
chess = [list(map(int, input().split())) for _ in range(n)]
color = [[0] * n for _ in range(n)]
black = []
white = []

for i in range(n):
    for j in range(n):
        color[i][j] = (i % 2 == 0 and j % 2 == 0) or (i % 2 != 0 and j % 2 != 0)
        if chess[i][j] == 1 and color[i][j]:
            black.append((i, j))
        
        if chess[i][j] == 1 and not color[i][j]:
            white.append((i, j))

down_right = [0] * (n*2 - 1)
up_right = [0] * (n*2 - 1)

black_count = 0
white_count = 0

def backtracking(bishop, idx, count):
    global black_count, white_count
    if idx == len(bishop):
        rx, ry = bishop[idx - 1]
        if color[rx][ry]:
            black_count = max(black_count, count)
        else:
            white_count = max(white_count, count)
        return
    
    x, y = bishop[idx]
    if down_right[x+y] or up_right[x-y+n-1]:
        backtracking(bishop, idx+1, count)
    else:
        down_right[x+y] = 1
        up_right[x-y+n-1] = 1
        backtracking(bishop, idx+1, count+1)
        down_right[x+y] = 0
        up_right[x-y+n-1] = 0
        backtracking(bishop, idx+1, count)

if len(black) > 0:
    backtracking(black, 0, 0)
if len(white) > 0:
    backtracking(white, 0, 0)
print(black_count + white_count)