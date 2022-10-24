class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n_count = {x:0 for x in range(1,len(nums)+1)}
        result = [-1, -1]
        for num in nums:
            n_count[num] += 1
        
        for k, v in n_count.items():
            if v == 0:
                result[1] = k
            if v == 2:
                result[0] = k
        return result
            