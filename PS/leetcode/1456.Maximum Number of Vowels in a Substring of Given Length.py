class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        
        curr = 0

        for char in s[:k]:
            if char in {'a','e','i','o','u'}:
                curr += 1
        
        answer = curr
        for i in range(1, len(s) - k + 1):
            if s[i-1] in {'a','e','i','o','u'}:
                curr -= 1
            
            if s[i+k-1] in {'a','e','i','o','u'}:
                curr += 1
            answer = max(answer, curr)
        return answer