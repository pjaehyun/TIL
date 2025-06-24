class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        n = len(nums)
        answer = set()
        
        idxs = []
        for i in range(n):
            if nums[i] == key:
                idxs.append(i)
        while idxs:
            curr = idxs.pop()
            l, r = max(0,curr - k), min(curr + k + 1, n)

            for i in range(l, r):
                answer.add(i)
        answer = sorted(list(answer))
        return answer
