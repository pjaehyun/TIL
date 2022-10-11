class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        # k가 i보다 작거나 같을 때 i=k
        # j는 i보다 무조건 크기때문에 i는 i보다 작거나 같은값으로 바뀌어도된다.
        # k가 j보다 크면 i < j < k가 성립하게 된다.
        
        i, j = float('inf'), float('inf')
        for k in nums:
            if k > j: return True  
            if k <= i: i = k 
            else: j = k      
        return False