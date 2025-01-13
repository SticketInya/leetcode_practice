from typing import List, Tuple

import pytest
from solution import Solution


class TestValidAnagram:

    def test_is_anagram(self):
        tests: List[Tuple[List[str], int]] = [
            (["2", "1", "+", "3", "*"], 9),
            (["4", "13", "5", "/", "+"], 6),
            (["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"], 22),
        ]

        for tokens, want in tests:
            got = Solution().eval_RPN(tokens)
            assert want == got
