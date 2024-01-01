# 첫번째 풀이
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        i, j, result = 0, 0, 0

        while i < len(g) and j < len(s):
            if g[i] <= s[j]:
                i, result = i + 1, result + 1
            j = j + 1
        return result

# 두번째 풀이
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        s.sort()

        answer = 0
        heapq.heapify(g)
        i = 0
        while g and i < len(s):
            if g[0] <= s[i]:
                answer += 1
                heapq.heappop(g)
            i += 1
        return answer