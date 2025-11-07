from typing import List

class Solution:
    def canAchieve(self, target: int, r: int, kAvailable: int, n: int, cityPower: List[int]) -> bool:
        diffArray = [0] * n
        runningAdd = 0

        for i in range(n):
            runningAdd += diffArray[i]
            currentPower = cityPower[i] + runningAdd

            if currentPower < target:
                need = target - currentPower
                kAvailable -= need
                if kAvailable < 0:
                    return False

                runningAdd += need
                if i + 2 * r + 1 < n:
                    diffArray[i + 2 * r + 1] -= need

        return True

    def maxPower(self, stations: List[int], r: int, k: int) -> int:
        n = len(stations)
        cityPower = [0] * n

        # Step 1: Compute initial power per city using prefix sums
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + stations[i]

        for i in range(n):
            left = max(0, i - r)
            right = min(n - 1, i + r)
            cityPower[i] = prefix[right + 1] - prefix[left]

        # Step 2: Binary search for the maximum possible minimum power
        low = min(cityPower)
        high = max(cityPower) + k
        best = 0

        while low <= high:
            mid = (low + high) // 2
            if self.canAchieve(mid, r, k, n, cityPower):
                best = mid
                low = mid + 1
            else:
                high = mid - 1

        return best