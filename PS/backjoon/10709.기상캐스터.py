import sys
input = sys.stdin.readline

h, w = map(int, input().split())

sky = [input().strip() for _ in range(h)]

answer = [[-1] * w for _ in range(h)]

for i in range(h):
    for j in range(w):
        if sky[i][j] == 'c':
            answer[i][j] = 0

for i in range(h):
    for j in range(1, w):
        if answer[i][j] == 0: continue
        if answer[i][j-1] != -1:
            answer[i][j] = answer[i][j-1] + 1
for a in answer:
    print(*a)