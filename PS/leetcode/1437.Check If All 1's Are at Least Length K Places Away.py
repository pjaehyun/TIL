class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        n = len(nums)

        curr = -1

        for i in range(n):
            if nums[i] == 1:
                if curr != -1:
                    if i - curr - 1 < k: return False
                curr = i
        return True