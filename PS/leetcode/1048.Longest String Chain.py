class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        dp = {}
        words.sort(key=lambda x:len(x))
        answer = 0
        for word in words:
            dp[word] = 1
            for i in range(len(word)):
                prev_word = word[:i] + word[i+1:]
                if prev_word in dp:
                    dp[word] = max(dp[word], dp[prev_word] + 1)
            answer = max(answer, dp[word])
        return answer