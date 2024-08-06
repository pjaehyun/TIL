class Solution:
    def minimumPushes(self, word: str) -> int:
        word_count = sorted([(x, y) for x, y in Counter(word).items()], key=lambda x:x[1], reverse=True)
        
        answer = 0

        for i in range(1, len(word_count)+1):
            answer += (ceil(i / 8) * word_count[i-1][1])
        return answer