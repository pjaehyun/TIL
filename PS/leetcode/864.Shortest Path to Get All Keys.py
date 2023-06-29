# 첫번째 풀이
class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        m, n = len(grid), len(grid[0])
        dq = deque()
        visited = set()
        keys_count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "@":
                    dq.append((i, j, ""))
                    visited.add((i, j, ""))
                if grid[i][j].islower():
                    keys_count += 1

        answer = 0
        while dq:
            size = len(dq)
            for _ in range(size):
                x, y, key = dq.popleft()
                if len(key) == keys_count:
                    return answer
                for xx, yy in [[x-1,y],[x,y+1],[x+1,y],[x,y-1]]:
                    if 0 <= xx < m and 0 <= yy < n and (xx, yy, key) not in visited and grid[xx][yy] != '#':
                        if grid[xx][yy] in "ABCEDF" and grid[xx][yy].lower() not in key:
                            continue
                        elif grid[xx][yy] in "abcdef" and grid[xx][yy] not in key:
                            dq.append((xx, yy, key + grid[xx][yy]))
                            visited.add((xx, yy, key + grid[xx][yy]))
                        else:
                            dq.append((xx, yy, key))
                            visited.add((xx, yy, key))
            answer += 1
        return -1

# 두번째 풀이(다른 해설 참고 Bit Manipulation을 이용하여 문제 풀이) 
class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        m, n = len(grid), len(grid[0])
        dq = deque()
        visited = set()
        keys_count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "@":
                    dq.append((i, j, 0))
                    visited.add((i, j, 0))
                if grid[i][j].islower():
                    keys_count += 1

        answer = 0
        while dq:
            size = len(dq)
            for _ in range(size):
                x, y, key = dq.popleft()
                if grid[x][y].islower():
                    key |= 1 << (ord(grid[x][y]) - ord('a'))
                    print(key)
                if key == (1 << keys_count) - 1:
                    return answer
                for xx, yy in [[x-1,y],[x,y+1],[x+1,y],[x,y-1]]:
                    if 0 <= xx < m and 0 <= yy < n and (xx, yy, key) not in visited and grid[xx][yy] != '#':
                        if grid[xx][yy].isupper() and key & (1 << (ord(grid[xx][yy]) - ord('A'))) == 0:
                            continue
                        dq.append((xx, yy, key))
                        visited.add((xx, yy, key))
            answer += 1
        return -1