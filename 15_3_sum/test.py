from typing import List, Tuple
from solution import Solution


class TestThreeSum:

    def testThreeSum(self):
        tests: List[Tuple[List[int], List[List[int]]]] = [
            ([-1, 0, 1, 2, -1, -4], [[-1, -1, 2], [-1, 0, 1]]),
            ([0, 1, 1], []),
            ([0, 0, 0], [[0, 0, 0]]),
        ]

        for nums, want in tests:
            got = Solution().threeSum(nums)
            assert sorted(want) == sorted(got)
