from typing import List, Tuple

import pytest
from solution import Solution


class TestCarFleet:

    def testCarFleet(self):
        tests: List[Tuple[int, List[int], List[int], int]] = [
            (12, [10, 8, 0, 5, 3], [2, 4, 1, 1, 3], 3),
            (10, [3], [3], 1),
            (100, [0, 2, 4], [4, 2, 1], 1),
            (10, [6, 8], [3, 2], 2),
            (10, [8, 3, 7, 4, 6, 5], [4, 4, 4, 4, 4, 4], 6),
        ]

        for n, positions, speeds, want in tests:
            got = Solution().carFleet(n, positions, speeds)
            assert want == got
