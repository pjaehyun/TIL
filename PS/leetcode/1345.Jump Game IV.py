class Solution:
    def minJumps(self, arr: List[int]) -> int:
        n = len(arr)

        numbers = defaultdict(list)

        for i in range(n):
            numbers[arr[i]].append(i)

        dq = deque()
        dq.append((0, 0))
        visited = [False for _ in range(n)]
        visited[0] = True

        while dq:
            for _ in range(len(dq)):
                i, step = dq.popleft()

                if i == n - 1:
                    return step

                if i + 1 < n and not visited[i+1]:
                    dq.append((i+1, step+1))
                    visited[i+1] = True
                
                if i - 1 >= 0 and not visited[i-1]:
                    dq.append((i-1, step+1))
                    visited[i-1] = True
                
                for j in numbers[arr[i]]:
                    if arr[i] == arr[j] and not visited[j]:
                        dq.append((j, step+1))
                        visited[j] = True
                numbers[arr[i]] = []
