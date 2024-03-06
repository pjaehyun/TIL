import sys
input = sys.stdin.readline

n, m = map(int, input().split())

lst = [list(input().strip()) for _ in range(n)]
answer = 1
for i in range(n):
    for j in range(m):
        for k in range(j+1, m):
            if lst[i][j] == lst[i][k]:
                dist = k - j
                if i + dist < n and lst[i+dist][k] == lst[i][j] and lst[i+dist][j] == lst[i][j]:
                    answer = max(answer, (dist+1) * (dist+1))
print(answer)