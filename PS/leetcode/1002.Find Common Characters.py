class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        answer = []

        for char in range(ord('a'), ord('z') + 1):
            char = chr(char)
            min_count = float('inf')

            for word in words:
                count = word.count(char)
                min_count = min(min_count, count)
                if min_count == 0:
                    break
            answer.extend([char] * min_count)
        return answer