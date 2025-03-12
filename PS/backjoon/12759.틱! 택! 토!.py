import sys
input = sys.stdin.readline

def judge():    
    for i in range(3):
        if arr[i][0] and arr[i][0] == arr[i][1] == arr[i][2]: return True
        if arr[0][i] and arr[0][i] == arr[1][i] == arr[2][i]: return True
    if arr[0][0] and arr[0][0] == arr[1][1] == arr[2][2]: return True
    if arr[0][2] and arr[0][2] == arr[1][1] == arr[2][0]: return True
    return False

player = int(input()) - 1
arr = [[0] * 3 for _ in range(3)]
draw = True

for _ in range(9):
    x, y = map(int, input().split())

    if player == 1:
        arr[x-1][y-1] = 2
    else:
        arr[x-1][y-1] = 1
    if judge():
        print(player+1)
        draw = False
        break
    player ^= 1

if draw: print(0)