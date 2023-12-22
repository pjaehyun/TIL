class Solution:
    def maxScore(self, s: str) -> int:
        l_count = 0
        r_count = 0

        l, r = 0, 1

        if s[l] == '0':
            l_count += 1
        
        for i in range(r, len(s)):
            if s[i] == '1':
                r_count += 1
        
        answer = l_count + r_count

        while r < len(s) - 1:
            if s[r] == '1':
                r_count -= 1
            else:
                l_count += 1
            
            l += 1
            r += 1
            answer = max(answer, l_count + r_count)
        return answer