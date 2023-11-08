class Solution:
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
        if sx == fx and sy == fy:
            return t > 1 or t == 0
        
        height_diff = abs(sy - fy)
        width_diff = abs(sx - fx)

        extra_time = abs(height_diff - width_diff)

        return (min(height_diff, width_diff) + extra_time) <= t