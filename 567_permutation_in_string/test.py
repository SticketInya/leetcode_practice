from typing import List, Tuple
from solution import Solution


class TestPermutationInString:

    def testCheckInclusion(self):
        tests: List[Tuple[str, str, bool]] = [
            ("ab", "eidbaooo", True),
            ("ab", "eidboaoo", False),
            ("adc", "dcda", True),
        ]

        for s1, s2, want in tests:
            got = Solution().checkInclusion(s1, s2)
            assert want == got
