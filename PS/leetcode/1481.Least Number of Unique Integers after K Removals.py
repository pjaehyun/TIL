class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        count = deque(sorted([(k, v) for k, v in Counter(arr).items()], key=lambda x:x[1]))
        while count and k >= count[0][1]:
            temp = count.popleft()
            k -= temp[1]
        return len(count)
        