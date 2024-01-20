# 첫번째 풀이(Monotonic stack)
class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        stack, answer = [], [0] * len(arr)
        
        for i, n in enumerate(arr):
            while stack and arr[stack[-1]] > n:
                stack.pop()
            j = stack[-1] if stack else -1
            answer[i] = answer[j] + (i - j) * n
            stack.append(i)
        return sum(answer) % 1000000007

# 두번째 풀이(Segment Tree)
class SegmentTree:
    def __init__(self, n, arr):
        self.arr = arr
        self.tree = [None] * (4 * n + 1)
        self.build(0, n-1, 0)
    
    def build(self, start, end, node):
        if start == end:
            self.tree[node] = start
            return
        
        mid = (start + end) // 2

        self.build(start, mid, node*2+1)
        self.build(mid+1, end, node*2+2)
        
        if self.arr[self.tree[node*2+1]] < self.arr[self.tree[node*2+2]]:
            self.tree[node] = self.tree[node*2+1]
        else: self.tree[node] = self.tree[node*2+2]
        
    def findMin(self, start, end, node, l, r):
        if l <= start and r >= end:
            return self.tree[node]
        if r < start or l > end:
            return None
        mid = (start + end) // 2
        
        m1 = self.findMin(start, mid, node*2+1, l, r)
        m2 = self.findMin(mid+1, end, node*2+2, l, r)

        if m1 is None:
            return m2
        elif m2 is None:
            return m1
        elif self.arr[m1] < self.arr[m2]:
            return m1
        else:
            return m2
    
    def find(self, l, r):
        return self.findMin(0, len(self.arr)-1, 0, l, r)

class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        st = SegmentTree(len(arr), arr)
        answer = self.sumMins(0, len(arr) - 1, st)
        return answer
    
    def sumMins(self, l, r, s):
        mod = (10**9+7)
        if l == r:
            return s.arr[l]
        
        min_idx = s.find(l, r)
        
        if min_idx is None:
            return 0
        _sum = (((min_idx - l + 1) * (r - min_idx + 1) % mod) * s.arr[min_idx]) % mod;
        s1 = self.sumMins(l, min_idx - 1, s)
        s2 = self.sumMins(min_idx + 1, r, s)

        _sum = ((s1 + s2)%mod + _sum) % mod
        return _sum
