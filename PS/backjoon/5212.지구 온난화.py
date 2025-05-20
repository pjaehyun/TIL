import sys
input = sys.stdin.readline

def sink(x, y):
    seas = 0
    for nx, ny in [(x+1,y),(x,y+1),(x-1,y),(x,y-1)]:
        if nx < 0 or nx >= r or ny < 0 or ny >= c:
            seas += 1
            continue
        if sea[nx][ny] == '.': seas += 1
    
    if seas >= 3:
        return True
    return False

r, c = map(int, input().split())

sea = [list(input().strip()) for _ in range(r)]

sub = []

for i in range(r):
    for j in range(c):
        if sea[i][j] == 'X' and sink(i, j):
            sub.append((i, j))

for x,y in sub:
    sea[x][y] = '.'

x1, y1, x2, y2 = float('inf'), float('inf'), float('-inf'), float('-inf')

for i in range(r):
    for j in range(c):
        if sea[i][j] == 'X':
            if j < x1: x1 = j
            if j > x2 : x2 = j
            if i < y1: y1 = i
            if i > y2: y2 = i

answer = [['.'] * (x2-x1+1) for _ in range(y2-y1+1)]

for i in range(r):
    for j in range(c):
        if sea[i][j] == 'X':
            answer[i-y1][j-x1] = 'X'

for a in answer:
    print(''.join(a))