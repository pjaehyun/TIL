class Solution:
    def nextBeautifulNumber(self, n: int) -> int:
        def counting(x):
            count = Counter(x)

            for k, v in count.items():
                if int(k) != v: return False
            return True

        for i in range(n+1, (10**6 * 2 + 1)):
            if counting(str(i)):
                return i