class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        prefixSum = 0
        
        dic = defaultdict(int)
        dic[0]=1
        answer = 0
        
        for n in nums:
            prefixSum += n

            mod = prefixSum % k
            answer += dic[mod]
            dic[mod] += 1
        return answer
