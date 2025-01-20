import math
from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if h == len(piles):
            return max(piles)

        left, right = 1, max(piles)
        possible = max(piles)

        while left < right:
            k = (left + right) // 2

            total_hours = 0
            for pile in piles:
                total_hours += math.ceil(pile / k)

            if total_hours > h:
                left = k + 1
            else:
                possible = k
                right = k - 1

        return possible
