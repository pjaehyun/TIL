class Solution:
    def minimumLength(self, s: str) -> int:
        l, r = 0, len(s) - 1

        while l < r:
            if s[l] == s[r]:
                l_temp = l
                while l_temp + 1 < len(s) and s[l_temp] == s[l_temp+1]:
                    l_temp += 1
                l = l_temp
                
                r_temp = r
                while r_temp - 1 >= 0 and s[r_temp] == s[r_temp-1]:
                    r_temp -= 1
                r = r_temp
                l += 1
                r -= 1
            else:
                break
        return r - l + 1 if r >= l else 0