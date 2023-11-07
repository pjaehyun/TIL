class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        minute = 0

        monsters = [dist[i] / speed[i] for i in range(len(dist))]
        monsters.sort()
        
        for i in range(len(monsters)):
            if monsters[i] <= i:
                return i
        return len(dist)