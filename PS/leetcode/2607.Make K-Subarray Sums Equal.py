class Solution:
    def makeSubKSumEqual(self, arr: List[int], k: int) -> int:
        n = len(arr)
        
        def gcd(x, y):
          value = 0

          for i in range(1, y + 1):
            if x % i == 0 and y % i == 0:
                value = i
          return value
        
        gcd = gcd(n, k)
        answer = 0
        for i in range(gcd):
          temp = sorted([arr[x] for x in range(i, n, gcd)])          
          mid = temp[len(temp) // 2]
          answer += sum(abs(mid - temp[j]) for j in range(len(temp)))
        return answer