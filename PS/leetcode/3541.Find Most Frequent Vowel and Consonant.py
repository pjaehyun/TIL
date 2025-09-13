class Solution(object):
    def maxFreqSum(self, s):
        freq = [0] * 26
        maxVowel, maxConso = 0, 0
        for c in s:
            i = ord(c) - ord('a')
            freq[i] += 1
            if c in 'aeiou':
                maxVowel = max(maxVowel, freq[i])
            else:
                maxConso = max(maxConso, freq[i])
        return maxVowel + maxConso