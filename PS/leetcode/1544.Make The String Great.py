class Solution:
    def makeGood(self, s: str) -> str:
        dq = deque(list(s))
        result = []
        while dq:
            char = dq.popleft()
            if result and abs(ord(result[-1]) - ord(char)) == 32:
                result.pop()
                continue
            else:
                result.append(char) 
        return ''.join(result)
                