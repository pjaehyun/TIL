class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        temp = sorted([(k, v) for k, v in Counter(nums).items()], key=lambda x:(x[1], -x[0]))
        answer = []

        for k, v in temp:
            for i in range(v):
                answer.append(k)
        return answer