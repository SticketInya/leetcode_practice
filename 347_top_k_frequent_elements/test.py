from typing import List, Tuple
import pytest
from solution import Solution


class TestTopKFrequentElements:

    def test_group_anagrams(self) -> None:
        tests: List[Tuple[List[int], int, List[int]]] = [
            ([1, 1, 1, 2, 2, 3], 2, [1, 2]),
            ([1], 1, [1]),
            ([4, 1, -1, 2, -1, 2, 3], 2, [2, -1]),
        ]

        for nums, k, output in tests:
            got = Solution().top_frequent_k(nums, k)
            if sorted(got) != sorted(output):
                pytest.fail(
                    f"Invalid result received for ({nums}, {k}); want={output}; got={got}!"
                )
