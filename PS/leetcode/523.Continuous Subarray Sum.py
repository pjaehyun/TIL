class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        _sum, dic = 0, {0:-1}
        for idx, num in enumerate(nums):
            # k현재까지 합계의 나머지
            _sum = (_sum + num) % k
            # 같은 나머지가 나온다면 이전에 나왔던 위치에서 현재까지 k의 배수가 더해진 것
            # 같은 나머지가 존재하는 위치가 현재 위치와 거리가 2이상이 되어야함:
            if _sum not in dic:
                dic[_sum] = idx
            elif idx - dic[_sum] >= 2:
                return True
        return False