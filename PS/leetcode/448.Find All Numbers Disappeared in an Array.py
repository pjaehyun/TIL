class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        
        arr = [0] * (n+1)
        answer = []

        for i in range(n):
            arr[nums[i]] = 1
        
        for i in range(1, n+1):
            if arr[i] == 0:
                answer.append(i)
        return answer
