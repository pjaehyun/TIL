class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        if len(dist) - 1 >= hour:
            return -1
        
        def search_dist(dist, n):
            total = 0

            for i in range(len(dist)):
                if i == len(dist) -  1:
                    total += dist[i] / n
                else: total += ceil(dist[i] / n)
            return total
        
        l, r = 1, 10**7
        while l <= r:
            mid = (l + r) // 2
            if search_dist(dist, mid) > hour:
                l = mid + 1
            else:
                r = mid - 1
        return l
