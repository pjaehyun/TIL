# 첫번째 풀이
class Solution:
    def countHomogenous(self, s: str) -> int:
        s = s + "$"
        l, r = 0, 0
        answer = 0
        while r < len(s):
            if s[l] == s[r]:
                r += 1
            else:
                answer += ((r - l) * (r - l + 1) // 2) % (10**9 + 7)
                l = r
        return answer

# 두번째 풀이
class Solution:
    def countHomogenous(self, s: str) -> int:
        mod = 10**9 + 7
        answer = 0
        prev = '$'
        count = 0
        for c in s:
            if c != prev:
                answer += (count * (count + 1) // 2) % mod
                count = 1
            else:
                
                count += 1
            prev = c
        answer += (count * (count + 1) // 2) % mod
        return answer