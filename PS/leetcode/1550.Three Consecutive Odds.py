class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        odd_count = 0
        for num in arr:
            if odd_count >= 3:
                return True
            if num % 2 != 0:
                odd_count += 1
            else:
                odd_count = 0
        if odd_count >= 3:
            return True
        return False