class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        count = Counter(nums)
        max_num_count = max(count.values())
        
        answer = [[] for _ in range(max_num_count)]

        for k, v in count.items():
            for i in range(v):
                answer[i].append(k)
        return answer