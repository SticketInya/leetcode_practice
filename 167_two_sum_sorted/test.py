from typing import List, Tuple
from solution import Solution


class TestTwoSumSorted:

    def testTwoSum(self):
        tests: List[Tuple[List[int], int, List[int]]] = [
            ([2, 7, 11, 15], 9, [1, 2]),
            ([2, 3, 4], 6, [1, 3]),
            ([-1, 0], -1, [1, 2]),
        ]

        for nums, target, want in tests:
            got = Solution().twoSum(nums, target)
            assert want == got
