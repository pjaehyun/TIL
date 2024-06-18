class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:

        def bs(x):
            l, r = 0, len(difficulty) - 1

            while l <= r:
                mid = (l + r) // 2

                if max_profit_for_difficulty[mid][0] <= x:
                    l = mid + 1
                else:
                    r = mid - 1
            return r

        infos = sorted(zip(difficulty, profit))
        max_profit_for_difficulty = []
        max_profit = 0
        for d, p in infos:
            max_profit = max(max_profit, p)
            max_profit_for_difficulty.append((d, max_profit))
        
        answer = 0

        for i in range(len(worker)):
            idx = bs(worker[i])
            if idx != -1 and worker[i] >= max_profit_for_difficulty[idx][0]:
                answer += max_profit_for_difficulty[idx][1]
        return answer