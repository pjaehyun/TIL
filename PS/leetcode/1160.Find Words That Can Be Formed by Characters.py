class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:

        def check(word, counts):
            c = [0] * 26

            for ch in word:
                t = ord(ch) - ord('a')
                c[t] += 1
                if c[t] > counts[t]:
                    return False
            return True
        counts = [0] * 26

        for c in chars:
            counts[ord(c) - ord('a')] += 1
        
        result = 0

        for word in words:
            if check(word, counts):
                result += len(word)
        return result
