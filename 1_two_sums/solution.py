from typing import List


class Solution(object):
    def two_sum(self, nums: List[int], target: int) -> List[str]:
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        seen: dict[int, int] = {}
        for i, el in enumerate(nums):
            diff = target - el
            if diff in seen:
                return [i, seen[diff]]
            else:
                seen[el] = i

        return [-1, -1]
