class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row, col = len(board), len(board[0])
        visited = [[False] * col for _ in range(row)]
        def dfs(x,y,s):
            if s == len(word):
                return True
            if x < 0 or x > row-1 or y < 0 or y > col-1 or word[s] != board[x][y] or visited[x][y]:
                return False
            visited[x][y] = True
            res = (dfs(x+1,y, s+1) or dfs(x,y+1, s+1) or
                   dfs(x-1,y, s+1) or dfs(x,y-1, s+1))
            visited[x][y] = False
            return res
        for i in range(row):
            for j in range(col):
                if dfs(i,j,0):
                    return True
        return False