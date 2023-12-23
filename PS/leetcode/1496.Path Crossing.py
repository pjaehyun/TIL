class Solution:
    def isPathCrossing(self, path: str) -> bool:
        direction = {"N": (0, 1), "E": (1, 0), "S": (0, -1), "W": (-1, 0)}
        
        visited = set()
        visited.add((0, 0))
        cur_x, cur_y = 0, 0
        for p in path:
            cur_x, cur_y = direction[p][0] + cur_x, direction[p][1] + cur_y
            
            if (cur_x, cur_y) in visited:
                return True
            visited.add((cur_x, cur_y))
        return False
