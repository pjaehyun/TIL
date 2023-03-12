import sys

input = sys.stdin.readline

N = int(input())

row = [0] * N
visited = [False] * N
answer = 0

def check(n):
    for i in range(n):
        if row[n] == row[i] or (abs(row[n] - row[i]) == abs(n - i)):
            return False
    return True

def dfs(n):
    global answer
    if n == N:
        answer += 1
        return
    for i in range(N):
        if not visited[n]:
            row[n] = i
            if check(n):
                visited[n] = True
                dfs(n+1)
                visited[n] = False
dfs(0)
print(answer)
    