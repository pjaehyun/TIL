class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        
        answer = 0

        for num in nums:
            if num % 3 != 0:
                answer += 1
        return answer