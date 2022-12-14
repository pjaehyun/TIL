import sys, math

input = sys.stdin.readline

N = int(input())
minus, zero, one = 0, 0, 0

square = [list(map(int, input().split())) for _ in range(N)]

def recursion(x, y, N):
    global minus, zero, one
    check = square[x][y]
    for i in range(x, x+N):
        for j in range(y, y+N):
            if check != square[i][j]:
                for k in range(3):
                    for z in range(3):
                        recursion(x+(N//3*k),y+(N//3*z),N//3)
                return
    if check == -1:
        minus += 1
    elif check == 0:
        zero += 1
    else:
        one += 1

recursion(0, 0, N)
print(minus)
print(zero)
print(one)