class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        temp = sorted(heights)
        answer = 0
        for i in range(len(heights)):
            if heights[i] != temp[i]:
                answer += 1
        return answer