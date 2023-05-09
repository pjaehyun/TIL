import sys

input = sys.stdin.readline

N = int(input())

mod = 10**9 + 7

def mul(matrix1, matrix2):
    res = [[0] * 2 for _ in range(2)]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                res[i][j] += matrix1[i][k] * matrix2[k][j]
            res[i][j] %= mod
    return res

def devide(n, matrix):
    if n == 1:
        return matrix
    else:
        temp = devide(n//2, matrix)
        if n % 2 == 0:
            return mul(temp, temp)
        else:
            return mul(mul(temp, temp), matrix)

matrix = [[1, 1], [1, 0]]
if N - 1 < 2:
    print(1)
else:
    print(devide(N-1, matrix)[0][0])
