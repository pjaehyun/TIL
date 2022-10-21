class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_count = []
        result = []
        for key, value in dict(Counter(nums)).items():
            nums_count.append((key, value))
        nums_count.sort(key=lambda x:x[1], reverse=True)
        for i in range(k):
            result.append(nums_count[i][0])
        return result