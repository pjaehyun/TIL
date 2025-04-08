class Solution:
    def minimumOperations(self, nums: List[int]) -> int:

        def is_duplicate(arr):
            check = defaultdict(int)

            for e in arr:
                check[e] += 1
                if check[e] > 1:
                    return True
            return False
        answer = 0
        is_dup = is_duplicate(nums)
        
        while is_dup:
            if is_duplicate(nums):
                for _ in range(3):
                    if nums:
                        nums.pop(0)
                answer += 1
            else:
                is_dup = False
        return answer
            