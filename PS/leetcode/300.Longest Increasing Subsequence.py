class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        temp = [nums[0]]
        answer = 1

        for i in range(1, len(nums)):
            if temp[-1] < nums[i]:
                temp.append(nums[i])
                answer += 1
            else:
                index = bisect.bisect_left(temp, nums[i])
                temp[index] = nums[i]
        return answer