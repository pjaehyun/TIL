class Solution:
    def minDeletions(self, s: str) -> int:
        count = Counter(s)
        
        exist = set()
        answer = 0
        for k, v in count.items():
            while v and v in exist:
                answer += 1
                v -= 1
            exist.add(v)
        return answer