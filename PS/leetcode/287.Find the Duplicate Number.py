# 첫번째 풀이
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        count = [0] * (len(nums) + 1)
        for num in nums:
            count[num] += 1
            if count[num] > 1:
                return num
        return len(nums)
            
# 두번째 풀이
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        tortoise = nums[0]
        hare = nums[0]

        while True:
            tortoise = nums[tortoise]
            hare = nums[nums[hare]]
            if tortoise == hare:
                break
        
        tortoise = nums[0]
        while tortoise != hare:
            tortoise = nums[tortoise]
            hare = nums[hare]
        return tortoise