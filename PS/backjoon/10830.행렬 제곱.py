import sys

input = sys.stdin.readline

N, B = map(int, input().split())

mat = []

for _ in range(N):
    mat.append(list(map(int, input().split())))

def mul(n, mat1, mat2):
    temp = [[0] * n for _ in range(N)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                temp[i][j] += mat1[i][k] * mat2[k][j]
            temp[i][j] %= 1000
    return temp

def devide(n, b, mat):
    if b == 1:
        return mat
    else:
        temp = devide(n, b//2, mat)
        if b % 2 == 0:
            return mul(n, temp, temp)
        else:
            return mul(n, mul(n, temp, temp), mat)
answer = devide(N, B, mat)
for i in range(N):
    for j in range(N):
        print(answer[i][j] % 1000, end =" ")
    print()