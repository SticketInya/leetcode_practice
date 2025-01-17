from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        numbers = nums
        index_mod = 0
        while numbers:
            midpoint = len(numbers) // 2
            if numbers[midpoint] < target:
                numbers = numbers[midpoint + 1 :]
                index_mod += midpoint + 1
            elif numbers[midpoint] > target:
                numbers = numbers[:midpoint]
            else:
                return index_mod + midpoint

        return -1

    def searchTwoPointers(self, nums: List[int], target: int) -> int:
        if len(nums) == 1:
            return -1 if nums[0] != target else 0

        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return -1
