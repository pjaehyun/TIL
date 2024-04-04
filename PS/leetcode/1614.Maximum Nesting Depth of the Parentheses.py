class Solution:
    def maxDepth(self, s: str) -> int:
        
        depth = 0
        answer = 0
        for c in s:
            if c == "(":
                depth += 1
            elif c == ")":
                answer = max(answer, depth)
                depth -= 1
        return answer