def solution(wallpaper):
    u, d, l, r = len(wallpaper)-1, 0, len(wallpaper[0])-1, 0
    x, y = [], []
    for i in range(len(wallpaper)):
        for j in range(len(wallpaper[0])):
            if wallpaper[i][j] == '#':
                x.append(i)
                y.append(j)
    return [min(x), min(y), max(x)+1, max(y)+1]
