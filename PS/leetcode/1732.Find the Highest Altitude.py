class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        answer = max(0, gain[0])
        for i in range(1, len(gain)):
            gain[i] = gain[i-1] + gain[i]
            answer = max(answer, gain[i])
        return answer
            