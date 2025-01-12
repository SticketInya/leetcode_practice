from typing import List, Tuple
import pytest
from solution import Solution


class TestProductOfArrayExceptSelf:

    def test_product_except_self(self) -> None:
        tests: List[Tuple[List[int]], List[int]] = [
            (
                [1, 2, 3, 4],
                [24, 12, 8, 6],
            ),
            (
                [-1, 1, 0, -3, 3],
                [0, 0, 9, 0, 0],
            ),
        ]

        for nums, want in tests:
            got = Solution().product_except_self(nums)
            assert want == got

    def test_product_except_self_division(self) -> None:
        tests: List[Tuple[List[int]], List[int]] = [
            (
                [1, 2, 3, 4],
                [24, 12, 8, 6],
            ),
            (
                [-1, 1, 0, -3, 3],
                [0, 0, 9, 0, 0],
            ),
            (
                [-1, 1, 0, -3, 0],
                [0, 0, 0, 0, 0],
            ),
        ]

        for nums, want in tests:
            got = Solution().product_except_self_division(nums)
            assert want == got
