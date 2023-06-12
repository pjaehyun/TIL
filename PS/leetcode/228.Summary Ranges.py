class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if len(nums) <= 1:
            return [str(x) for x in nums]
        x, y = 0, 0
        answer = []
        for i in range(1, len(nums) + 1):
            if i < len(nums) and nums[y]+1 == nums[i]:
                y += 1
            else:
                if y - x > 0:
                    answer.append(f"{nums[x]}->{nums[y]}")
                else:
                    answer.append(str(nums[x]))
                x, y = i, i
        return answer
