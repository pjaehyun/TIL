import sys
input = sys.stdin.readline

k, r, n = map(str, input().split())

k_x, k_y = int(k[1]) - 1, ord(k[0]) - 65
r_x, r_y = int(r[1]) - 1, ord(r[0]) - 65
n = int(n)
for _ in range(n):
    m = input().strip()
    
    t_x, t_y = k_x, k_y
    if m == "R":
        if k_y + 1 < 8:
            k_y += 1
    elif m == "L":
        if k_y - 1 >= 0:
            k_y -= 1
    elif m == "T":
        if k_x + 1 < 8:
            k_x += 1
    elif m == "B":
        if k_x - 1 >= 0:
            k_x -= 1
    elif m == "RB":
        if k_y + 1 < 8 and k_x - 1 >= 0:
            k_y += 1
            k_x -= 1
    elif m == "LB":
        if k_y - 1 >= 0 and k_x - 1 >= 0:
            k_y -= 1
            k_x -= 1
    elif m == "RT":
        if k_y + 1 < 8 and k_x + 1 < 8:
            k_y += 1
            k_x += 1
    elif m == "LT":
        if k_y - 1 >= 0 and k_x + 1 < 8:
            k_y -= 1
            k_x += 1

    if k_x == r_x and k_y == r_y:
        if 0<=r_y + (k_y - t_y)<8 and 0<=r_x + (k_x - t_x)<8:
            r_x, r_y = r_x + (k_x - t_x), r_y + (k_y - t_y)
        else:
            k_x, k_y = t_x, t_y
print(chr(k_y+65)+str(k_x+1))
print(chr(r_y+65)+str(r_x+1))