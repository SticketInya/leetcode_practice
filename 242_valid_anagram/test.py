from typing import List, Tuple

import pytest
from solution import Solution


class TestValidAnagram:

    def test_is_anagram(self):
        tests: List[Tuple[str, str, bool]] = [
            ("anagram", "nagaram", True),
            ("rat", "car", False),
        ]

        for s, t, output in tests:
            got = Solution().is_anagram(s, t)
            if got != output:
                pytest.fail(
                    f"Invalid result received for ({s},{t}); want={output}; got={got}!"
                )
