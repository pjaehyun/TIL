class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        answer = float('inf')
        for i in range(0, len(blocks)-k+1):
            temp = blocks[i:i+k]
            res = 0
            for j in range(k):
                if temp[j] == "W":
                    res += 1
            answer = min(answer, res)
        return answer