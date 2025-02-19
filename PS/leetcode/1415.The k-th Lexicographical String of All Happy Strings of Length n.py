class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        alp = ['a','b','c']

        answer = []

        def bt(s):
            if len(s) == n:
                answer.append(s)
                return
            for c in alp:
                if s[-1] != c:
                    bt(s+c)
        for c in alp:
            bt(c)
        if k > len(answer):
            return ""
        return answer[k-1]