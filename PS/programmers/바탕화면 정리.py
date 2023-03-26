# 첫번째 풀이
def solution(wallpaper):
    u, d, l, r = len(wallpaper)-1, 0, len(wallpaper[0])-1, 0
    for i in range(len(wallpaper)):
        for j in range(len(wallpaper[0])):
            if wallpaper[i][j] == '#':
                if i < u:
                    u = i
                if i > d:
                    d = i
                if j < l:
                    l = j
                if j > r:
                    r = j
    return [u, l, d+1, r+1]

# 두번째 풀이(코드 개선)
def solution(wallpaper):
    x, y = [], []
    for i in range(len(wallpaper)):
        for j in range(len(wallpaper[0])):
            if wallpaper[i][j] == '#':
                x.append(i)
                y.append(j)
    return [min(x), min(y), max(x)+1, max(y)+1]
