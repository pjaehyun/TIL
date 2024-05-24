class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:

        def backtracking(idx, temp):
            nonlocal answer
            for i in range(26):
                if letters_count[i] > count[i]:
                    return
            
            answer = max(answer, temp)

            for i in range(idx, len(words)):
                for c in words[i]:
                    letters_count[ord(c) - ord('a')] += 1
                    temp += score[ord(c) - ord('a')]
                
                backtracking(i+1, temp)

                for c in words[i]:
                    letters_count[ord(c) - ord('a')] -= 1
                    temp -= score[ord(c) - ord('a')]
                    
        count = [0] * 26
        letters_count = [0] * 26

        for c in letters:
            count[ord(c) - ord('a')] += 1
        
        answer = 0
        backtracking(0, 0)
        return answer
