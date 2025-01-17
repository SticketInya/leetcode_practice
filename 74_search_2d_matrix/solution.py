from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left, right, up, down = 0, len(matrix[0]) - 1, 0, len(matrix) - 1

        while left <= right and up <= down:
            current_row = (up + down) // 2
            # If the target is one of the current pointers
            if (
                matrix[current_row][left] == target
                or matrix[current_row][right] == target
            ):
                return True
            # If the target should be within the current row
            elif (
                matrix[current_row][left] < target
                and matrix[current_row][right] > target
            ):
                # Binary search within the row
                mid = (left + right) // 2
                if matrix[current_row][mid] == target:
                    return True
                elif matrix[current_row][mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            # If the target is in a row below (lower index) of the current row
            elif matrix[current_row][left] > target:
                down = current_row - 1
            # If the target is in a row above (higher index) of the current row
            else:
                up = current_row + 1

        return False
