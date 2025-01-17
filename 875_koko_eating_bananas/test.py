from typing import List, Tuple
from solution import Solution


class TestKokoEatingBananas:

    def testMinEatingSpeed(self):
        tests: List[Tuple[List[int], int, int]] = [
            ([3, 6, 7, 11], 8, 4),
            ([30, 11, 23, 4, 20], 5, 30),
            ([30, 11, 23, 4, 20], 6, 23),
            ([312884470], 312884469, 2),
            (
                [
                    332484035,
                    524908576,
                    855865114,
                    632922376,
                    222257295,
                    690155293,
                    112677673,
                    679580077,
                    337406589,
                    290818316,
                    877337160,
                    901728858,
                    679284947,
                    688210097,
                    692137887,
                    718203285,
                    629455728,
                    941802184,
                ],
                823855818,
                14,
            ),
        ]

        for piles, hours, want in tests:
            got = Solution().minEatingSpeed(piles, hours)
            assert want == got
