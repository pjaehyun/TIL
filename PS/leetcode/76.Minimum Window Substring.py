class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t = Counter(t)
        _max, count = inf, len(t)
        start, end = 0, 0
        result = ""
        
        while end < len(s):
            # find end point
            while end < len(s) and count != 0:
                if s[end] in t:
                    t[s[end]] -= 1
                    if t[s[end]] == 0:
                        count -= 1
                end += 1

            # find start point
            while start <= end and count == 0:
                if _max > end - start:
                    _max = end-start
                    result = s[start:end]
                if s[start] in t:
                    t[s[start]] += 1
                    if t[s[start]] > 0:
                        count += 1
                start += 1
        return result
