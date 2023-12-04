class Solution:
    def largestGoodInteger(self, num: str) -> str:
        l, r = 0, 0
        answer = ""
        while r < len(num):
            if num[l] == num[r]:
                r += 1
            else:
                if r - l >= 3:
                    answer = max(answer, num[l:l+3])
                l = r
        if r - l >= 3:
            answer = max(answer, num[l:l+3])
        return answer