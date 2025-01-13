from typing import List, Tuple
import pytest
from solution import Solution


class TestValidParentheses:

    def test_is_valid(self) -> None:
        tests: List[Tuple[str], bool] = [
            ("()", True),
            ("()[]{}", True),
            ("(]", False),
            ("([])", True),
        ]

        for brackets, want in tests:
            got = Solution().is_valid(brackets)
            assert want == got

    def test_is_valid_stack(self) -> None:
        tests: List[Tuple[str], bool] = [
            ("()", True),
            ("()[]{}", True),
            ("(]", False),
            ("([])", True),
        ]

        for brackets, want in tests:
            got = Solution().is_valid(brackets)
            assert want == got
