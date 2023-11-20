class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        visited = set()

        travel_time = 0
        collect_time = 0

        idx = len(garbage) - 1
        while garbage:
            house = garbage.pop()
            collect_time += len(house)
            for trash in house:
                if trash not in visited:
                    travel_time += sum(travel[:idx])
                    visited.add(trash)
            
            idx -= 1
        return travel_time + collect_time