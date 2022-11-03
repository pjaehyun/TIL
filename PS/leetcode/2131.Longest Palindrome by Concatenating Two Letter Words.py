class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        counter = Counter(words)
        result = mid = 0
        string = ""
        for word in counter.keys():
            if word[0] == word[1]:
                result += counter[word] if counter[word] % 2 == 0 else counter[word] - 1
                mid |= counter[word] % 2
            elif word[::-1] in counter:
                result += min(counter[word], counter[word[::-1]])
        return (result+mid)*2
