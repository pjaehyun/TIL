# 첫번째 풀이 
class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        rec1 = (ax2 - ax1) * (ay2 - ay1)
        rec2 = (bx2 - bx1) * (by2 - by1)
        itst = 0

        cx1, cx2 = max(ax1, bx1), min(ax2, bx2)
        cy1, cy2 = max(ay1, by1), min(ay2, by2)
        if cx1 < cx2 and cy1 < cy2:
            itst = (cx2 - cx1) * (cy2 - cy1)
        return rec1 + rec2 - itst

# 두번째 풀이(그냥 이해하기 쉬운 코드로 작성해봄)
class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        rec1 = (ax2 - ax1) * (ay2 - ay1)
        rec2 = (bx2 - bx1) * (by2 - by1)
        rec3 = 0

        ax_plane = set([x for x in range(ax1, ax2+1)])
        ay_plane = set([x for x in range(ay1, ay2+1)])

        bx_plane = set([x for x in range(bx1, bx2+1)])
        by_plane = set([x for x in range(by1, by2+1)])
        
        intersection_x_plane = list(ax_plane & bx_plane)
        intersection_y_plane = list(ay_plane & by_plane)

        if intersection_x_plane and intersection_y_plane:
            cx1, cx2 = min(intersection_x_plane), max(intersection_x_plane)
            cy1, cy2 = min(intersection_y_plane), max(intersection_y_plane)
            rec3 = (cx2 - cx1) * (cy2 - cy1)
        return rec1 + rec2 - rec3