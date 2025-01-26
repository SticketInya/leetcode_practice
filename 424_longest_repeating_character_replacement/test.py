from typing import List, Tuple
from solution import Solution


class TestLongestRepeatingCharacterReplacement:

    def testCharacterReplacement(self) -> None:
        tests: List[Tuple[str, int, int]] = [
            ("ABAB", 2, 4),
            ("AABABBA", 1, 4),
            ("ABAB", 0, 1),
        ]

        for s, k, want in tests:
            got = Solution().characterReplacement(s, k)
            assert want == got

    def testCharacterReplacementOptimized(self) -> None:
        tests: List[Tuple[str, int, int]] = [
            ("ABAB", 2, 4),
            ("AABABBA", 1, 4),
            ("ABAB", 0, 1),
        ]

        for s, k, want in tests:
            got = Solution().characterReplacementOptimized(s, k)
            assert want == got
