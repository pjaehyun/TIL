class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        p = 1 << n
        nums.sort()
        answer = []

        for i in range(p):
            temp = []
            for j in range(n):
                if i & 1 << j:
                    temp.append(nums[j])
            answer.append(temp)
        return answer
