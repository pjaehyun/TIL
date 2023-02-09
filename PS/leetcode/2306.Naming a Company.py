class Solution:
    def distinctNames(self, ideas: List[str]) -> int:
        answer = 0
        
        names = [set() for i in range(26)]

        for idea in ideas:
            names[ord(idea[0]) - ord('a')].add(idea[1:])
        
        for i in range(25):
            for j in range(i+1, 26):
                count = len(names[i] & names[j])
                
                answer += 2*(len(names[i])-count)*(len(names[j])-count)
        return answer