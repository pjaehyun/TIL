import sys
input = sys.stdin.readline

n = int(input())

move = input().strip()

foot_print = []

max_x, min_x, max_y, min_y = 0, 0, 0, 0

direction = {0:(1,0),1:(0,-1),2:(-1,0),3:(0,1)}

idx = 0

curr = [0, 0]
 
for m in move:
    if m == "R":
        idx = (idx + 1) % 4
    elif m == "L":
        idx = (idx + 3) % 4
    else:
        nx, ny = curr[0] + direction[idx][0], curr[1] + direction[idx][1]
        curr = [nx, ny]
        foot_print.append(curr)

        max_x = max(max_x, nx)
        min_x = min(min_x, nx)
        max_y = max(max_y, ny)
        min_y = min(min_y, ny)

r, c = max_x - min_x + 1, max_y - min_y + 1

graph = [['#'] * c for _ in range(r)]
foot_print.append((0, 0))

for x, y in foot_print:
    graph[x-min_x][y-min_y] = '.'
for g in graph:
    print(''.join(g))