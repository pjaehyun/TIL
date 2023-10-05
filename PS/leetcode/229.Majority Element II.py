class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        freq = len(nums) / 3
        
        nums.sort()

        i, j = 0, 0
        answer = []

        while j < len(nums):
            if nums[i] == nums[j]:
                j += 1
            else:
                if j - i > freq:
                    answer.append(nums[i])
                i = j
                j = i + 1
        if j - i > freq:
            answer.append(nums[i])
        return answer