class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        answer = 0
        prefix = 0
        dic = {0:1}

        for num in nums:
            prefix += num

            if prefix-k in dic:
                answer += dic[prefix-k]

            if prefix not in dic:
                dic[prefix] = 1
            else:
                dic[prefix] += 1
        return answer