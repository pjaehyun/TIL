# 첫번째 풀이
class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        
        n = len(scores)

        dp = [0] * n

        temp = sorted(zip(ages, scores))

        for i in range(n):
            age, score = temp[i]
            dp[i] = score

            for j in range(i):
                if temp[j][1] <= score:
                    dp[i] = max(dp[i], dp[j] + score)
        return max(dp)


# 두번째 풀이(다른 사람 풀이 참고)
class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        
        dp = [0] * (1+max(ages))

        temp = sorted(zip(scores,ages))
        for i in range(len(scores)):
            score, age = temp[i]

            dp[age] = score + max(dp[:age+1])

        return max(dp)