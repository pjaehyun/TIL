class WordDictionary:

    def __init__(self):
        self.trie = {}

    def addWord(self, word: str) -> None:
        current = self.trie
        for w in word:
            if w not in current:
                current[w] = {}
            current = current[w]
        current['#'] = True
        
    def search(self, word: str) -> bool:
                
        return self.dfs(self.trie, word)
    
    def dfs(self, node, word):
        if not word:
            return '#' in node
        
        if word[0] == '.':
            for child in node:
                if child != '#' and self.dfs(node[child], word[1:]):
                    return True
        elif word[0] in node:
            return self.dfs(node[word[0]], word[1:])
        return False
# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)