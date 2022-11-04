class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = {'a','e','i','o','u','A','E','I','O','U'}
        s = list(s)
        i, j = 0, len(s) - 1

        while i < j:
            if s[i] in vowels and s[j] not in vowels:
                j -= 1
                continue
            elif s[i] not in vowels and s[j] in vowels:
                i += 1
                continue
            elif s[i] in vowels and s[j] in vowels:
                s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1
        return ''.join(s)
