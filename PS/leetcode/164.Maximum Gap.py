# 첫번째 풀이(통과는 하지만 제약조건 미준수)
class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        nums.sort()
        answer = 0

        for i in range(len(nums) - 1):
            answer = max(answer, nums[i+1] - nums[i])
        return answer
    
# 두번째 풀이(제약조건 준수 Bucket Sort 활용 다른 문제 참고)
class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        
        n, low, high = len(nums), min(nums), max(nums)
        
        if n <= 1:
            return 0

        bucket_size = max(1, (high - low) // (n - 1))
        buckets_num = (high - low) // bucket_size + 1
        
        buckets = [None] * buckets_num
        print(buckets)
        for num in nums:
            idx = (num - low) // bucket_size
            if not buckets[idx]:
                buckets[idx] = {'min': num, 'max': num}
            else:
                buckets[idx]['min'] = min(buckets[idx]['min'], num)
                buckets[idx]['max'] = max(buckets[idx]['max'], num)
        
        answer = 0
        prev = low
        for bucket in buckets:
            if bucket:
                answer = max(answer, bucket['min'] - prev)
                prev = bucket['max']
        return answer