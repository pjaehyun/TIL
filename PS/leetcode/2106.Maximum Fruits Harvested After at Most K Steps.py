class Solution:
    def maxTotalFruits(self, fruits: List[List[int]], startPos: int, k: int) -> int:
        def step(R, L):
            return min(startPos-2*L+R, 2*R-startPos-L)
        i0=bisect.bisect_left(fruits, [startPos-k, 0])
        iN=bisect.bisect_right(fruits, [startPos+k+1,-1])

        ans, wsum, l=0, 0, i0
        for r in range(i0, iN):
            wsum+=fruits[r][1]
            R=fruits[r][0]
            while l<=r and step(R, fruits[l][0])>k:
                wsum-=fruits[l][1]
                l+=1
            ans=max(ans, wsum)
        return ans
        
        