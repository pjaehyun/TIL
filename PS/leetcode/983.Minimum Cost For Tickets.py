class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        dp = [0] * 366
        
        days = set(days)
        for i in range(1, 366):
            if i not in days:
                # i가 여행 날짜에 없으면 이전 값을 가져옴
                dp[i] = dp[i-1]
            else:
                # dp[i-1] + costs[0: 1day 티켓으로 이전값에 티켓값만 더해줌
                # dp[max(0, i-7)] + costs[1]: 7day 티켓으로 7일전의 값과 티켓값을 더해줌
                # dp[max(0, i-30)] + costs[2]: 30day 티켓으로 30일 전의 값과 티켓값을 더해줌
                dp[i] = min(dp[i-1] + costs[0], dp[max(0, i-7)] + costs[1], dp[max(0, i-30)] + costs[2])
        return dp[-1]
                