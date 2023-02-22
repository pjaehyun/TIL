class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        low = max(weights)
        high = sum(weights)
        
        while low < high:
            mid = (low + high) // 2
            day = 1
            temp = 0
            for weight in weights:
                if temp + weight > mid:
                    day += 1
                    temp = weight
                else:
                    temp += weight
            if day <= days:
                high = mid
            else:
                low = mid + 1
        return low