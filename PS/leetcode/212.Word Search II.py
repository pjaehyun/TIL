# 백트래킹 + Trie자료구조

class Trie:
    def __init__(self):
        self.trie = {}
        
    def insert(self, word):
        current = self.trie
        for w in word:
            if w not in current:
                current[w] = {}
            current = current[w]
        current['#'] = '#'
        
    def remove(self, word):
        current = self.trie
        nodes = []
        for w in word:
            if w not in current:
                return False
            current = current[w]
            nodes.append((current, w))
        
        if '#' in current:
            remove = '#'
            for node, w in nodes[::-1]:
                if remove == '#' or len(node[remove]) == 0: del(node[remove])
                remove = w

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
        row, col = len(board), len(board[0])
        result = set()
        root = Trie()
        visited = [[False] * col for _ in range(row)]
        
        for w in words:
            root.insert(w)

        def dfs(x, y, word, trie):
            if x < 0 or x >= row or y < 0 or y >= col or visited[x][y] or board[x][y] not in trie:
                return
            visited[x][y] = True
            word = word + board[x][y]
            trie = trie[board[x][y]]
            if '#' in trie:
                result.add(word)
                root.remove(word)
            for i in range(4):
                xx, yy = x + dx[i], y + dy[i]
                dfs(xx, yy, word, trie)
            visited[x][y] = False

        for i in range(row):
            for j in range(col):
                dfs(i, j, "", root.trie)
        return list(result)