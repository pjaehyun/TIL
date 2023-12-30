class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        n = len(words)
        count = defaultdict(int)

        for i in range(n):
            for j in range(len(words[i])):
                count[words[i][j]] += 1
        
        for k, v in count.items():
            if v % n != 0:
                return False
        return True