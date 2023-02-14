class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        answer = []

        for i in range(n):
            answer.append(nums[i])
            answer.append(nums[n+i])
        return answer