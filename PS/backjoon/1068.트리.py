import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
remove = int(input())


def dfs(x):
    arr[x] = -99
    for i in range(n):
        if x == arr[i]:
            dfs(i)

dfs(remove)

answer = 0
for i in range(n):
    if arr[i] != -99 and i not in arr:
        answer += 1
print(answer)