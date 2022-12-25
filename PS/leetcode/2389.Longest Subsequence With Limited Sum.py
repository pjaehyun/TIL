class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        pre = []
        pre.append(0)

        for n in nums:
            pre.append(pre[-1] + n)
        
        answer = []
        for q in queries:
            _max = 0
            for i in range(1, len(pre)):
                if pre[i] <= q:
                    _max = i
            answer.append(_max)
        return answer
                    