class Solution:
    def getWordsInLongestSubsequence(self, n: int, words: List[str], groups: List[int]) -> List[str]:
            
        dp = [1] * n
        pv = [-1] * n
        for i in range(1, n):
            for j in range(i):
                if groups[i] != groups[j] and len(words[i]) == len(words[j]) and sum(a != b for a, b in zip(words[i], words[j])) == 1:
                    if dp[j]+ 1 > dp[i]:
                        dp[i] = dp[j] + 1
                        pv[i] = j
        
        wi = dp.index(max(dp))
        answer = []
        
        while wi != -1:
            answer.append(words[wi])
            wi = pv[wi]
        
        return answer[::-1]