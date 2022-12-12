N = int(input())

graph = [list(map(int, input().split())) for _ in range(N)]
white, color = [], []
def dev_and_con(x, y, N):
    check = graph[x][y]
    for i in range(x, x+N):
        for j in range(y, y+N):
            if check != graph[i][j]:
                dev_and_con(x, y, N//2)
                dev_and_con(x, y+(N//2), N//2)
                dev_and_con(x+(N//2), y, N//2)
                dev_and_con(x+(N//2), y+(N//2), N//2)
                return
    if check == 0:
        white.append(0)
    else:
        color.append(1)
dev_and_con(0, 0, N)
print(len(white))
print(len(color))