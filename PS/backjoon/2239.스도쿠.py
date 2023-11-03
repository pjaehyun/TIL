import sys
input = sys.stdin.readline
sys.setrecursionlimit = 1000000

arr = [[int(x) for x in list(input().strip())] for _ in range(9)]

def check(x, y, value):
    if value in arr[x]:
        return False
    
    for i in range(9):
        if value == arr[i][y]:
            return False
        
    for i in range(3):
        for j in range(3):
            if value == arr[x // 3 * 3 + i][y//3 * 3 + j]:
                return False
    return True

def bt(n):
    if n == len(blank):
        for a in arr:
            for e in a:
                print(e, end="")
            print()
        exit()

    for i in range(1, 10):
        x = blank[n][0]
        y = blank[n][1]

        if check(x, y, i):
            arr[x][y] = i
            bt(n+1)
            arr[x][y] = 0

blank = []

for i in range(9):
    for j in range(9):
        if arr[i][j] == 0:
            blank.append((i, j))
bt(0)