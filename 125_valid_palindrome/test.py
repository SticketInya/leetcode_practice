from typing import List, Tuple
from solution import Solution


class TestLargestRectangleArea:

    def testLargestRectangleArea(self):
        tests: List[Tuple[str, bool]] = [
            ("A man, a plan, a canal: Panama", True),
            ("race a car", False),
            (" ", True),
        ]

        for text, want in tests:
            got = Solution().isPalindrome(text)
            assert want == got
