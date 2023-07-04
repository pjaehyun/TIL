# 첫번째 풀이(완전 탐색)
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        count = defaultdict(int)

        for num in nums:
            count[num] += 1
        
        for k, v in count.items():
            if v == 1:
                return k
        return -1

# 두번째 풀이(비트연산 풀이 참고)
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ones = 0
        twos = 0

        for num in nums:
            ones = (ones^num) & (~twos)
            twos = (twos^num) & (~ones)
        return ones