class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        m = len(l)
        answer = []
        for i in range(m):
            temp = nums[l[i]:r[i]+1]
            temp.sort()
            diff = temp[0] - temp[1]
            flag = True
            for j in range(2, len(temp)):
                if temp[j-1] - temp[j] != diff:
                    answer.append(False)
                    flag = False
                    break
            if flag:
                answer.append(True)
        return answer
