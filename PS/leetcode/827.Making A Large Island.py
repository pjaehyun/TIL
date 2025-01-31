class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        def is_valid_coordinates(r, c):
            return 0 <= r < m and 0 <= c < n 

        group_area = {}
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        def dfs(i, j, group):
            grid[i][j] = group
            group_area[group] += 1
            for di, dj in directions:
                ni, nj = i + di, j + dj
                if is_valid_coordinates(ni, nj) and grid[ni][nj] == 1:
                    dfs(ni, nj, group)

        group = 2        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    group_area[group] = 0
                    dfs(i, j, group)
                    group += 1

        if not group_area:
            return 1

        max_area = max(group_area.values())

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    neighboring_groups = set()
                    for di, dj in directions:
                        ni, nj = i + di, j + dj
                        if is_valid_coordinates(ni, nj) and grid[ni][nj] != 0:
                            neighboring_groups.add(grid[ni][nj])
                    combined_area = 1 + sum(group_area[group] for group in neighboring_groups)
                    max_area = max(max_area, combined_area)

        return max_area