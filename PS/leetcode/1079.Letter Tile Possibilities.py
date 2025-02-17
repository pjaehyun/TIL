class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        def bt(x, idx):
            if is_tile[x] < 1:
                is_tile[x] += 1
            for i in range(n):
                if i == idx:
                    continue
                if not visited[i]:
                    visited[i] = True
                    bt(x + tiles[i], i)
                    visited[i] = False
        
        n = len(tiles)
        visited = [False] * n
        is_tile = defaultdict(int)

        for i in range(n):
            visited[i] = True
            bt(tiles[i], i)
            visited[i] = False
        return len(is_tile)