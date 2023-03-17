class Trie:

    def __init__(self):
        self.trie = {}

    def insert(self, word: str) -> None:
        current = self.trie
        for w in word:
            if w not in current:
                current[w] = {}
            current = current[w]
        current['#'] = '#'

    def search(self, word: str) -> bool:
        current = self.trie
        for w in word:
            if w not in current:
                return False
            current = current[w]
        if '#' in current:
            return True
        else:
            return False
                

    def startsWith(self, prefix: str) -> bool:
        current = self.trie
        for p in prefix:
            if p not in current:
                return False
            current = current[p]
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)