# 첫번째 코드
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # 3 x 3 박스에 같은 숫자가 들어가있거나
        # 한 라인에 같은 숫자가 들어가있는지 체크 3
        for i in range(9):
            sub_x = i + 3 - (i % 3)
            for j in range(9):
                if board[i][j] == '.':
                    continue

                # Horizontal
                horizontal = board[i]
                horizontal_count = 0
                horizontal_count = count(horizontal, board[i][j])
                if horizontal_count > 1:
                    return False

                # Vertical
                vertical = [x[j] for x in board]
                horizontal_count = 0
                vertical_count = count(vertical, board[i][j])
                if vertical_count > 1:
                    return False

                # 3 x 3 박스 확인    
                sub_y = j + 3 - (j % 3)
                each = [x[sub_y - 3:sub_y] for x in board[sub_x-3: sub_x]]
                box_count = 0
                box_count = count(sum(each, []), board[i][j])
                if box_count > 1:
                    return False
        return True
        
def count(arr, num):
    result = 0
    for a in arr:
        if a == num:
            result += 1
    return result


# 두번째 코드(시간 복잡도 개선)
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        vertical = [set() for _ in range(9)]
        horizontal = [set() for _ in range(9)]
        box = [set() for _ in range(9)]
        
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    continue
                
                # horizontal
                if board[i][j] in horizontal[i]:
                    print(board[i][j], horizontal[i])
                    return False
                horizontal[i].add(board[i][j])

                # vertical
                if board[i][j] in vertical[j]:
                    return False
                vertical[j].add(board[i][j])

                # box
                idx = (i // 3) * 3 + j // 3
                if board[i][j] in box[idx]:
                    return False
                box[idx].add(board[i][j])
        return True