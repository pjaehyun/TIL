class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n, m = len(haystack), len(needle)
        pi = [0 for _ in range(m)]
        
        for i in range(1, m):
            mid = (i+1) // 2
            left, right = mid, mid
            if (i+1) % 2 != 0:
                right += 1
            while left != 0:
                if needle[:left] == needle[right:i+1]:
                    pi[i] = left
                    break
                else:
                    left -= 1
                    right += 1
        j = 0
        for i in range(n):
            while j > 0 and haystack[i] != needle[j]:
                j += pi[j-1]
            if haystack[i] == needle[j]:
                j += 1
            if haystack[i:i+m] == needle:
                return i
        return -1