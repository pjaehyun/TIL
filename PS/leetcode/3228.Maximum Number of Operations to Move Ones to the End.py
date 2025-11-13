class Solution:
    def maxOperations(self, s: str) -> int:
        
        prev = 0
        answer = 0

        flag = True
        for i in range(len(s)):
            if s[i] == "0":
                if flag:
                    continue
                answer += prev
                flag = True
            else:
                prev += 1
                flag = False
        return answer
