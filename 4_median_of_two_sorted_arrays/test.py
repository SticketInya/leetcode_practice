from typing import List, Tuple
from solution import Solution


class TestMedianOfTwoSortedArrays:

    def testFindMedianSortedArrays(self):
        tests: List[Tuple[List[int], List[int], float]] = [
            ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5, 6, 7, 8], 4.0),
            ([1, 3], [4], 3.0),
            ([1, 2], [3, 4], 2.5),
        ]

        for nums1, nums2, want in tests:
            got = Solution().findMedianSortedArrays(nums1, nums2)
            assert want == got
