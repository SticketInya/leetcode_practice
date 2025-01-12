from collections import defaultdict
from typing import Dict, List, Tuple


class Solution:
    def is_valid_sudoku(self, board: List[List[str]]) -> bool:
        length = len(board)

        for row in board:
            seen: Dict[str, bool] = {}
            for cell in row:
                if cell == ".":
                    continue
                if cell in seen:
                    return False
                else:
                    seen[cell] = True

        for i in range(length):
            seen: Dict[str, bool] = {}
            for j in range(length):
                if board[j][i] == ".":
                    continue
                elif board[j][i] in seen:
                    return False
                else:
                    seen[board[j][i]] = True

        for i in range(0, length * 3, 3):
            col = i // length
            row_start = i % length
            rows = board[row_start : row_start + 3]
            nums: List[int] = []
            for row in rows:
                nums += row[col * 3 : col * 3 + 3]

            seen: Dict[str, bool] = {}
            for cell in nums:
                if cell == ".":
                    continue
                elif cell in seen:
                    return False
                else:
                    seen[cell] = True

        return True

    def is_valid_sudoku_single_pass(self, board: List[List[str]]) -> bool:
        rows: Dict[int, str] = defaultdict(str)
        cols: Dict[int, str] = defaultdict(str)
        squares: Dict[Tuple[int, int], str] = defaultdict(str)

        for r in range(9):
            for c in range(9):
                entry = board[r][c]
                if entry == ".":
                    continue
                elif entry in rows[r] or entry in cols[c]:
                    return False
                elif entry in squares[(r // 3, c // 3)]:
                    return False

                rows[r] += entry
                cols[c] += entry
                squares[(r // 3, c // 3)] += entry

        return True
