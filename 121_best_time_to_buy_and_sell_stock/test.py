from typing import List, Tuple
from solution import Solution


class TestBestTimeToBuyAndSellStock:

    def testMaxProfit(self) -> None:
        tests: List[Tuple[List[int], int]] = [
            ([7, 1, 5, 3, 6, 4], 5),
            ([7, 6, 4, 3, 1], 0),
            ([1, 2, 4], 3),
        ]

        for nums, want in tests:
            got = Solution().maxProfit(nums)
            assert want == got
