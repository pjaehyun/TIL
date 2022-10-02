class Solution:
    def maxArea(self, height: List[int]) -> int:
        i, j = 0, len(height)-1
        answer = 0
        
        while True:
            if i == j:
                break
            answer = max(answer, min(height[i], height[j]) * (j - i))
            if height[i] <= height[j]:
                i += 1
            elif height[j] < height[i]:
                j -= 1
        return answer