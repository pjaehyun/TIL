import sys
input = sys.stdin.readline

n = int(input())

tree = [[' '] * (n * 2) for _ in range(n)]

def recur(x, y, n):
    if n == 3:
        tree[x][y] = '*'
        tree[x+1][y-1] = tree[x+1][y+1] = '*'
        for i in range(-2, 3):
            tree[x+2][y+i] = '*'
    else:
        nextN = n // 2
        recur(x, y, nextN)
        recur(x+nextN, y+nextN, nextN)
        recur(x+nextN, y-nextN, nextN)

recur(0, n-1, n)
for t in tree:
    print(''.join(t))