class Solution:
    def compressedString(self, word: str) -> str:
        prev = word[0]
        count = 1

        answer = ""

        for i in range(1, len(word)):
            if prev == word[i] and count < 9:
                count += 1
            else:
                answer += str(count)
                answer += prev

                prev = word[i]
                count = 1
        answer += str(count)
        answer += prev
        return answer