from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1
        unique_nums = set(numbers)

        while left < right:
            if target - numbers[left] not in unique_nums:
                left += 1
                continue

            while left < right and numbers[left] + numbers[right] != target:
                right -= 1

            if numbers[left] + numbers[right] == target:
                return [left + 1, right + 1]

            left += 1
            right = len(numbers) - 1

        return [0, 0]
