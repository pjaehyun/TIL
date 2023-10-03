# 첫번째 풀이
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        answer = 0

        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] == nums[j]:
                    answer += 1
        return answer

# 두번째 풀이
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        counter = Counter(nums)
        answer = 0
        for v in counter.values():
            answer += math.comb(v, 2)
        return answer
        