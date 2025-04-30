import sys
input = sys.stdin.readline

t = int(input())

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

for _ in range(t):
    curr = 0
    x, y, min_x, min_y, max_x, max_y = 0, 0, 0, 0, 0, 0

    move = input().strip()

    for m in move:
        if m == "F":
            x += dx[curr]
            y += dy[curr]
        elif m == "B":
            x += dx[(curr+2) % 4]
            y += dy[(curr+2) % 4]
        elif m == "R":
            curr = (curr+1) % 4
        else:
            curr = (curr+3) % 4
            
        min_x = min(min_x, x)
        max_x = max(max_x, x)
        min_y = min(min_y, y)
        max_y = max(max_y, y)
    print(abs(max_x - min_x) * abs(max_y - min_y))
    