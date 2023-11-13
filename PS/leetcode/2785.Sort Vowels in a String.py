class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = "aeiouAEIOU"
        s = list(s)
        vowels_sort = []

        for c in s:
            if c in vowels:
                vowels_sort.append((ord(c), c))
        vowels_sort.sort()
        vowels_sort = deque(vowels_sort)
        for i in range(len(s)):
            if s[i] in vowels:
                s[i] = vowels_sort.popleft()[1]
        return ''.join(s)
