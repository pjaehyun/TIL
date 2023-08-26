class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort()
        
        answer = [pairs[0]]
        for i in range(1, len(pairs)):
            if pairs[i][0] < answer[-1][1] and pairs[i][1] < answer[-1][1]:
                answer.pop()
                answer.append(pairs[i])
            elif answer[-1][1] < pairs[i][0]:
                answer.append(pairs[i])
        return len(answer)