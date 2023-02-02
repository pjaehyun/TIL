class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        alien = {order[i]:i for i in range(len(order))}
        
        for i in range(len(words) - 1):
            if len(words[i+1]) < len(words[i]) and words[i+1] == words[i][:len(words[i+1])]:
                return False
            
            for j in range(len(words[i])):
                if j+1 > len(words[i+1]):
                    break
                if alien[words[i][j]] < alien[words[i+1][j]]:
                    break
                if alien[words[i][j]] > alien[words[i+1][j]]:
                    return False
                else:
                    continue
        return True