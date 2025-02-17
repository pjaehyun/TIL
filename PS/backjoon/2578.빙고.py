import sys
input = sys.stdin.readline

arr = [list(map(int, input().split())) for _ in range(5)]
arr_idx = {}

for i in range(5):
    for j in range(5):
        arr_idx[arr[i][j]] = (i, j)
def count_bingo():
    bingo = 0
    for i in range(5):
        temp = 0
        for j in range(5):
            if arr[i][j] == -1:
                temp += 1
        if temp >= 5: bingo += 1
    
    for i in range(5):
        temp = 0
        for j in range(5):
            if arr[j][i] == -1:
                temp += 1
        if temp >= 5: bingo += 1

    temp = 0
    for i in range(5):
        if arr[i][i] == -1:
            temp += 1
    if temp >= 5: bingo += 1

    temp = 0
    for i in range(5):
        if arr[i][4-i] == -1:
            temp += 1
    if temp >= 5: bingo += 1
    return bingo

mode = [list(map(int, input().split())) for _ in range(5)]

answer = 0
for i in range(5):
    for j in range(5):
        answer += 1
        arr[arr_idx[mode[i][j]][0]][arr_idx[mode[i][j]][1]] = -1
        res = count_bingo()
        if res >= 3:
            print(answer)
            exit(0)
