class Solution:
        def countTrapezoids(self, points: List[List[int]]) -> int:
            seen_points = []
            seen_parallel_lines = defaultdict(int)
            seen_same_lines = defaultdict(int)
            seen_parallel_line_sides = defaultdict(int)
            seen_same_line_sides = defaultdict(int)
            
            result = 0
            rhombuses = 0
            for x1, y1 in points:
                for x2, y2 in seen_points:
                    k = ((y1 - y2) / (x1 - x2)) if x1 - x2 != 0 else "inf"
                    b = (y1 - k * x1) if k != "inf" else x1
                    k = round(k, 8) if k != "inf" else k
                    b = round(b, 8)

                    slope_id = k
                    line_id = (k, b)
                    other_sides = seen_parallel_lines[slope_id] - seen_same_lines[line_id]
                    result += other_sides

                    seen_parallel_lines[slope_id] += 1
                    seen_same_lines[line_id] += 1

                    dx, dy = abs(x1 - x2), abs(y1 - y2)
                    side = dx * dx + dy * dy
                    rhombuses += seen_parallel_line_sides[(k, side)] - seen_same_line_sides[(k, b, side)]

                    seen_parallel_line_sides[(k, side)] += 1
                    seen_same_line_sides[(k, b, side)] += 1
                    
                seen_points.append((x1, y1))

            return result - rhombuses//2