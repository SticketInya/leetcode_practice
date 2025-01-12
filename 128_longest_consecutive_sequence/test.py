from typing import List, Tuple
import pytest
from solution import Solution


class TestLongestConsecutiveSequence:

    def test_valid_sudoku(self) -> None:
        tests: List[Tuple[List[int], int]] = [
            (
                [100, 4, 200, 1, 3, 2],
                4,
            ),
            (
                [0, 3, 7, 2, 5, 8, 4, 6, 0, 1],
                9,
            ),
        ]

        for nums, want in tests:
            got = Solution().longest_consecutive(nums)
            assert want == got
