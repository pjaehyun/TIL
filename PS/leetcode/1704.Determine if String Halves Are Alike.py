# 첫번째 풀이
class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        
        mid = len(s) // 2

        first_half_vowel = [x for x in s[:mid] if x in vowels]
        second_half_vowel = [x for x in s[mid:] if x in vowels]

        if len(first_half_vowel) == len(second_half_vowel):
            return True
        return False


# 두번째 풀이(코드 라인 줄이기)
class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        return len([char for char in s[:len(s) // 2].lower() if char in "aeiou"]) == len([char for char in s[len(s) // 2:].lower() if char in "aeiou"])