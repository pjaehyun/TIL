class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        answer = ""
        left = 0
        right = 0
        flag = 0

        for c in s:
            if c == "(":
                left += 1
                flag += 1
            elif c == ")" and flag > 0:
                right += 1
                flag -= 1
        
        k = min(left, right)
        left, right = k, k

        for c in s:
            if c == "(":
                if left > 0:
                    answer += "("
                    left -= 1
            elif c == ")":
                if right > 0 and right > left:
                    answer += ")"
                    right -= 1
            else:
                answer += c
        return answer