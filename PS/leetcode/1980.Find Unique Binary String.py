# 첫번째 풀이(칸토어 대각선 논법)
class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        answer = ""
        for i in range(len(nums)):
            if nums[i][i] == "1":
                answer += "0"
            else:
                answer += "1"
        return answer
    
# 두번째 풀이(백트래킹)
class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        def bt(n, b):
            if len(b) == n:
                if b in nums:
                    return None
                return b

            for j in range(2):
                b += str(j)
                next_b = bt(n, b)
                if next_b is not None:
                    return next_b
                b = b[:-1]
            return None
        return bt(len(nums), "")