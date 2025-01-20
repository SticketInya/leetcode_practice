from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        if nums[0] < nums[-1]:
            return nums[0]

        current_min = nums[0]
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] < current_min:
                current_min = nums[mid]
                right = mid - 1
            else:
                left = mid + 1

        return current_min
