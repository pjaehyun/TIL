class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        nums_dict = {}

        for i in range(len(nums)):
            if nums[i] in nums_dict and i - nums_dict[nums[i]] <= k:
                return True
            nums_dict[nums[i]] = i    
        return False