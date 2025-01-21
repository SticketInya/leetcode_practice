from typing import List, Tuple
from solution import Solution


class TestSearchInRotatedSortedArray:

    def testSearch(self):
        tests: List[Tuple[List[int], int, int]] = [
            ([4, 5, 6, 7, 0, 1, 2], 0, 4),
            ([4, 5, 6, 7, 0, 1, 2], 3, -1),
            ([4, 5, 6, 7, 0, 1, 2], 6, 2),
            ([1], 0, -1),
            ([1, 3, 5], 1, 0),
            ([3, 5, 1], 3, 0),
            ([5, 1, 3], 3, 2),
        ]

        for nums, target, want in tests:
            got = Solution().search(nums, target)
            assert want == got
