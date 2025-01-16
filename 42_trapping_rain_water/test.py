from typing import List, Tuple
from solution import Solution


class TestTrappingRainWater:

    def testTrap(self):
        tests: List[Tuple[List[int], int]] = [
            ([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1], 6),
            ([4, 2, 0, 3, 2, 5], 9),
            ([4, 2, 3], 1),
            ([9, 8, 2, 6], 4),
        ]

        for heights, want in tests:
            got = Solution().trap(heights)
            assert want == got

    def testTrapTwoPointers(self):
        tests: List[Tuple[List[int], int]] = [
            ([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1], 6),
            ([4, 2, 0, 3, 2, 5], 9),
            ([4, 2, 3], 1),
            ([9, 8, 2, 6], 4),
        ]

        for heights, want in tests:
            got = Solution().trapTwoPointers(heights)
            assert want == got
