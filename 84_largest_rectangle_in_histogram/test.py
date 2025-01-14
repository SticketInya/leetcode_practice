from typing import List, Tuple
from solution import Solution


class TestLargestRectangleArea:

    def testLargestRectangleArea(self):
        tests: List[Tuple[List[int], int]] = [
            ([2, 1, 5, 6, 2, 3], 10),
            ([2, 4], 4),
            ([2, 1, 2], 3),
            ([2, 2, 2], 6),
            ([2, 3], 4),
        ]

        for heights, want in tests:
            got = Solution().largestRectangleArea(heights)
            assert want == got
