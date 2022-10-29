# 완전탐색
from itertools import permutations
def solution(k, dungeons):
    dungeons = list(permutations(dungeons))
    result = [0] * len(dungeons)
    for i in range(len(dungeons)):
        fatigue = k
        for j in range(len(dungeons[i])):
            if dungeons[i][j][0] <= fatigue:
                result[i] += 1
                fatigue -= dungeons[i][j][1]
    return max(result)
        

# DFS(백트래킹)
answer = 0
visited = []

def dfs(k, count, dungeons):
    global answer
    
    if count > answer:
        answer = count
    
    for i in range(len(dungeons)):
        if k >= dungeons[i][0] and not visited[i]:
            visited[i] = True
            dfs(k - dungeons[i][1], count + 1, dungeons)
            visited[i] = False

def solution(k, dungeons):
    global visited
    visited = [False] * len(dungeons)
    dfs(k, 0, dungeons)
    return answer
