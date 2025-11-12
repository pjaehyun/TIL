class Solution:
    def minOperations(self, nums: List[int]) -> int:
        
        def gcd(x, y):
            if y > x:
                x, y = y, x
            
            while y:
                temp = x % y
                x = y
                y = temp
            return x

        ones = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                ones += 1
        if ones: return len(nums) - ones

        count = 0
        while True:
            temp = deepcopy(nums)
            for i in range(len(nums) - 1):
                nums[i] = gcd(nums[i], nums[i+1])
                if nums[i] == 1: return len(nums) + count
            if temp == nums:
                return -1
            count += 1
        return -1
