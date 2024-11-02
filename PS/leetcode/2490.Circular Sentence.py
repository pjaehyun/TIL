class Solution:
    def isCircularSentence(self, s: str) -> bool:
        if s[0]!=s[-1]: 
            return False
        split=-1
        while True:
            split=s.find(' ', split+1)
            if split==-1: 
                break
            if s[split-1]!=s[split+1]: 
                return False
        return True
        