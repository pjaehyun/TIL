N, M = map(int, input().split())

result = []
def dfs(start):
    if len(result) == M:
        print(' '.join(result))
        return
    for i in range(start, N + 1):
        if i not in result:
            result.append(str(i))
            dfs(i+1)
            f = result.pop()
dfs(1)