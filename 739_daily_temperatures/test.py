from typing import List, Tuple

import pytest
from solution import Solution


class TestDailyTemperatures:

    def testDailyTemperatures(self):
        tests: List[Tuple[List[int], List[int]]] = [
            ([73, 74, 75, 71, 69, 72, 76, 73], [1, 1, 4, 2, 1, 1, 0, 0]),
            ([30, 40, 50, 60], [1, 1, 1, 0]),
            ([30, 60, 90], [1, 1, 0]),
        ]

        for temps, want in tests:
            got = Solution().dailyTemperatures(temps)
            assert want == got

    def testDailyTemperatures2(self):
        tests: List[Tuple[List[int], List[int]]] = [
            ([73, 74, 75, 71, 69, 72, 76, 73], [1, 1, 4, 2, 1, 1, 0, 0]),
            ([30, 40, 50, 60], [1, 1, 1, 0]),
            ([30, 60, 90], [1, 1, 0]),
        ]

        for temps, want in tests:
            got = Solution().dailyTemperatures2(temps)
            assert want == got
