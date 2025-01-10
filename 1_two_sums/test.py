from typing import List, Tuple

import pytest
from solution import Solution


class TestTwoSum:

    def test_two_sum(self):
        tests: List[Tuple[List[int], int, List[int]]] = [
            ([2, 7, 11, 15], 9, [0, 1]),
            ([3, 2, 4], 6, [1, 2]),
            ([3, 3], 6, [0, 1]),
            ([-1, -2, -3, -4, -5], -8, [2, 4]),
        ]

        for numbers, target, output in tests:
            got = Solution().two_sum(numbers, target)
            for el in got:
                if el not in output:
                    pytest.fail(
                        f"Invalid result received for ({numbers},{target}); want={output}; got={got}!"
                    )
