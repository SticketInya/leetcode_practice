from typing import List, Tuple

import pytest
from solution import Solution


class TestContainsDuplicate:

    def test_contains_duplicate(self):
        tests: List[Tuple[List[int], bool]] = [
            ([1, 2, 3, 1], True),
            ([1, 2, 3, 4], False),
            ([1, 1, 1, 3, 3, 4, 3, 2, 4, 2], True),
        ]

        for input, output in tests:
            tc = Solution()
            got = tc.contains_duplicate(input)
            if output != got:
                pytest.fail(
                    f"Received invalid result for {input}; want={output}; got={got}!"
                )
