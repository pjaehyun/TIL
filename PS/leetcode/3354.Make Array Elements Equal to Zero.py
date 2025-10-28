class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        answer = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                l, r = sum(nums[:i]), sum(nums[i+1:])
                if l == r: answer += 2
                elif l + 1 == r or l == r+1: answer += 1
        return answer