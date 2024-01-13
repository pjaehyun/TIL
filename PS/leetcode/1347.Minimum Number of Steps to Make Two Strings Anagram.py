class Solution:
    def minSteps(self, s: str, t: str) -> int:
        s_count = Counter(s)
        t_count = Counter(t)

        answer = 0
        for k, v in t_count.items():
            if s_count[k] < v:
                answer += v - s_count[k]
        return answer