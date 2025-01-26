from typing import List, Tuple
from solution import Solution


class TestLongestSubstringWithoutRepeatingCharacters:

    def testLengthOfLongestSubstring(self) -> None:
        tests: List[Tuple[str, int]] = [
            ("abcabcbb", 3),
            ("bbbbb", 1),
            ("pwwkew", 3),
        ]

        for s, want in tests:
            got = Solution().lengthOfLongestSubstring(s)
            assert want == got
