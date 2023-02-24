# min heap과 max heap을 구분하여 풀이했을 때 시간초과
# 풀이 참조 후 max heap을 만드는 과정에서 최소값을 구해놓고
# max heap의 값을 pop할 때 마다 최대, 최소의 차이와 최솟값을 갱신 하는 방식으로 풀이
class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        answer = inf
        min_value = inf

        hq = []
        for num in nums:
            if num % 2 == 0:
                heapq.heappush(hq, -num)
                min_value = min(min_value, num)
            else:
                heapq.heappush(hq, -num * 2)
                min_value = min(min_value, num*2)
        
        while hq[0] % 2 == 0:
            max_value = -heapq.heappop(hq)
            answer = min(answer, max_value - min_value)
            num = max_value // 2
            heapq.heappush(hq, -num)
            min_value = min(min_value, num)

        answer = min(answer, -hq[0] - min_value)
        return answer
            