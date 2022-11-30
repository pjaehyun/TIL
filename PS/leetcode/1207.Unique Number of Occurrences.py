# 첫번째 풀이
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        return len(set([v for k,v in Counter(arr).items()])) == len(set(arr))

# 두번째 풀이(시간복잡도 개선)        
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        counter = Counter(arr)
        return len(set(counter.values())) == len(counter.keys())