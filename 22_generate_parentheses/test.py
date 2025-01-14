from typing import List, Tuple

import pytest
from solution import Solution


class TestGenerateParentheses:

    def testgenerateParenthesis(self):
        tests: List[Tuple[int, List[str]]] = [
            (3, ["((()))", "(()())", "(())()", "()(())", "()()()"]),
            (1, ["()"]),
        ]

        for n, want in tests:
            got = Solution().generateParenthesis(n)
            assert sorted(want) == sorted(got)

    def testgenerateParenthesisDFS(self):
        tests: List[Tuple[int, List[str]]] = [
            (3, ["((()))", "(()())", "(())()", "()(())", "()()()"]),
            (1, ["()"]),
        ]

        for n, want in tests:
            got = Solution().generateParenthesisDFS(n)
            assert sorted(want) == sorted(got)
