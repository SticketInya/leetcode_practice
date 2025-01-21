from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        current_min, index = nums[0], 0

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid

            if nums[mid] < current_min:
                current_min = nums[mid]
                index = mid
                right = mid - 1
            else:
                left = mid + 1

        if target <= nums[-1]:
            left, right = index, len(nums) - 1
        else:
            left, right = 0, index

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid

            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return -1
