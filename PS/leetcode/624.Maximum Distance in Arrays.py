class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        _min = float('inf')
        _max = -float('inf')
        answer = 0
        for array in arrays:
            answer = max(answer, max(array[-1] - _min, _max - array[0]))
            _min, _max = min(_min, array[0]), max(_max, array[-1])
        return answer
