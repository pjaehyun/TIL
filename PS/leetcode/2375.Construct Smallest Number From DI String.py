class Solution:
    def smallestNumber(self, pattern: str) -> str:
        pattern += "E"
        answer = ""

        num = 2
        dq = deque([1])
        temp = 1

        for i in range(1, len(pattern)):
            dq.append(num)
            if pattern[i-1] != pattern[i]:
                if pattern[i] == "E":
                    if pattern[i-1] == "I":
                        while dq: answer += str(dq.popleft())
                    else: 
                        while dq: answer += str(dq.pop())
                elif pattern[i-1] == "I":
                    for _ in range(temp):
                        x = dq.popleft()
                        answer += str(x)
                elif pattern[i-1] == "D":
                    for _ in range(temp):
                        x = dq.pop()
                        answer += str(x)
                temp = 1
            else:
                temp += 1
            num += 1
        return answer