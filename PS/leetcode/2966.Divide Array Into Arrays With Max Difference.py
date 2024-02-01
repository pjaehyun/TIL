class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()
        answer = []
        for i in range(3, len(nums)+1, 3):
            temp = nums[i-3:i]
            if temp[-1] - temp[0] > k:
                return []
            answer.append(temp)
        return answer