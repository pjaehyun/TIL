class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        n = len(nums)

        answer = []
        for i in range(n-k+1):
            xsum = 0
            count = sorted([(k, v) for k, v in Counter(nums[i:i+k]).items()], key=lambda x:(-x[1],-x[0]))
            
            for j in range(min(x, len(count))):
                xsum += (count[j][0] * count[j][1])
            answer.append(xsum)
        return answer