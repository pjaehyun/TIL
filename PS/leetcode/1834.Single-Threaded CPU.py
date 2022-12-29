# 첫번째 풀이
class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        n = len(tasks)

        tasks = [[item[0], item[1], idx] for idx, item in enumerate(tasks)]
        tasks.sort()
        start = 0

        min_heap = []
        answer = []
        while len(answer) < n:
            while tasks and tasks[0][0] <= start:
                work = tasks.pop(0)
                heapq.heappush(min_heap, [work[1], work[2]])
            if min_heap:
                process = heapq.heappop(min_heap)
                answer.append(process[1])
                start += process[0]
            else:
                start = tasks[0][0]
        return answer       

# 두번째 풀이(시간복잡도 개선)
class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        n = len(tasks)
        tasks = sorted([[item[0], item[1], idx] for idx, item in enumerate(tasks)])
        start = 0

        min_heap = []
        answer = []
        i = 0
        while len(answer) < n:
            while i < n and tasks[i][0] <= start:
                heapq.heappush(min_heap, [tasks[i][1], tasks[i][2]])
                i += 1
            if min_heap:
                process = heapq.heappop(min_heap)
                answer.append(process[1])
                start += process[0]
            else:
                start = tasks[i][0]
        return answer 