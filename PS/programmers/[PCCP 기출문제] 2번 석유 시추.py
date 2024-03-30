import sys
sys.setrecursionlimit(1000000)

def solution(land):
    def dfs(x, y, land_num):
        answer = 1 if land[x][y] != 1 else 0
        for nx, ny in [(x+1,y), (x,y+1), (x-1,y), (x,y-1)]:
            if 0 <= nx < len(land) and 0 <= ny < len(land[0]) and land[nx][ny] == 1:
                land[nx][ny] = land_num
                answer += dfs(nx, ny, land_num)
        return answer
    n, m = len(land), len(land[0])
    
    land_num = 2
    land_dict = {}
    for i in range(n):
        for j in range(m):
            if land[i][j] == 1:
                land[i][j] = land_num
                count = dfs(i, j, land_num)
                land_dict[land_num] = count
                land_num += 1
    answer = 0
    for j in range(m):
        visited = set()
        temp = 0
        for i in range(n):
            if land[i][j] not in visited:
                if land[i][j] != 0:
                    temp += land_dict[land[i][j]]
                    visited.add(land[i][j])
        answer = max(temp, answer)
    return answer