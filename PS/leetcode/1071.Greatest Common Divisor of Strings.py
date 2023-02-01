class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        answer = ""
        temp = ""

        for i in range(len(str1)):
            temp += str1[i]
            divide1 = len(str1) // len(temp)
            divide2 = len(str2) // len(temp)

            if temp * divide1 == str1 and temp * divide2 == str2:
                answer = temp
        return answer
            