class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        count = defaultdict(int)

        for num in nums:
            count[num] += 1
        
        for k, v in count.items():
            if v == 1:
                return k
        return -1