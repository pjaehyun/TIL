class Solution:
    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
        answer = 0

        for l in left:
            answer = max(answer, abs(0 - l))
        
        for r in right:
            answer = max(answer, abs(n - r))

        return answer