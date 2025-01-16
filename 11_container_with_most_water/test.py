from typing import List, Tuple
from solution import Solution


class TestContainerWithMostWater:

    def testmaxArea(self):
        tests: List[Tuple[List[int], int]] = [
            ([1, 8, 6, 2, 5, 4, 8, 3, 7], 49),
            ([1, 1], 1),
        ]

        for nums, want in tests:
            got = Solution().maxArea(nums)
            assert want == got
