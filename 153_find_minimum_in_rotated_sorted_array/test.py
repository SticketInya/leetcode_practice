from typing import List, Tuple
from solution import Solution


class TestFindMinimumInRotatedSortedArray:

    def testFindMin(self):
        tests: List[Tuple[List[int], int]] = [
            ([3, 4, 5, 1, 2], 1),
            ([4, 5, 6, 7, 0, 1, 2], 0),
            ([11, 13, 15, 17], 11),
        ]

        for nums, want in tests:
            got = Solution().findMin(nums)
            assert want == got
