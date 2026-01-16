class Solution:
    def maximizeSquareArea(self, m: int, n: int, hFences: List[int], vFences: List[int]) -> int:
        hFences.extend([1, m])
        vFences.extend([1, n])

        stt = set()
        ans = 0

        for i in range(len(hFences)):
            for j in range(i+1, len(hFences)):
                stt.add(abs(hFences[j]-hFences[i]))
        
        for i in range(len(vFences)):
            for j in range(i+1, len(vFences)):
                val = abs(vFences[j]-vFences[i])
                if val in stt:
                    ans = max(ans, val)
        
        if ans == 0:
            return -1
        return (ans*ans)%(10**9+7)