import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())

board = [input().strip() for _ in range(n)]

dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]

rx, ry = 0, 0
bx, by = 0, 0
for i in range(n):
    for j in range(m):
        if board[i][j] == 'R':
            rx, ry = i, j
        elif board[i][j] == 'B':
            bx, by = i, j

def move(x, y, i, j):
    count = 0
    while board[x+i][y+j] != '#' and board[x][y] != 'O':
        x += i
        y += j
        count += 1
    return x, y, count

def bfs(ri, rj, bi, bj):
    dq = deque()    
    visited = set()

    dq.append((ri, rj, bi, bj, 1))
    visited.add((ri, rj, bi, bj))

    while dq:
        rx, ry, bx, by, step = dq.popleft()

        if step > 10:
            break

        for i in range(4):
            nrx, nry, rstep = move(rx, ry, dx[i], dy[i])
            nbx, nby, bstep = move(bx, by, dx[i], dy[i])

            if board[nbx][nby] == 'O':
                continue

            if board[nrx][nry] == 'O':
                return step
            
            if nrx == nbx and nry == nby:
                if rstep > bstep:
                    nrx -= dx[i]
                    nry -= dy[i]
                else:
                    nbx -= dx[i]
                    nby -= dy[i]
            
            if (nrx, nry, nbx, nby) not in visited:
                visited.add((nrx, nry, nbx, nby))
                dq.append((nrx, nry, nbx, nby, step+1))
    return -1

print(bfs(rx, ry, bx, by))