from typing import List, Tuple
from solution import Solution


class TestBinarySearch:

    def testSearch(self):
        tests: List[Tuple[List[int], int, int]] = [
            ([-1, 0, 3, 5, 9, 12], 9, 4),
            ([-1, 0, 3, 5, 9, 12], 2, -1),
        ]

        for nums, target, want in tests:
            got = Solution().search(nums, target)
            assert want == got

    def testSearchTwoPointers(self):
        tests: List[Tuple[List[int], int, int]] = [
            ([-1, 0, 3, 5, 9, 12], 9, 4),
            ([-1, 0, 3, 5, 9, 12], 2, -1),
            ([2, 5], 2, 0),
            ([2, 5], 5, 1),
            ([5], 5, 0),
        ]

        for nums, target, want in tests:
            got = Solution().searchTwoPointers(nums, target)
            assert want == got
