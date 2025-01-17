from typing import List, Tuple
from solution import Solution


class TestSearch2DMatrix:

    def testSearch(self):
        tests: List[Tuple[List[List[int]], int, bool]] = [
            ([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 3, True),
            ([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 13, False),
            ([[1]], 1, True),
            ([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 50]], 5, True),
        ]

        for matrix, target, want in tests:
            got = Solution().searchMatrix(matrix, target)
            assert want == got
