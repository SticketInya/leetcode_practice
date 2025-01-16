from typing import List, Tuple


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        valid_sums = set[Tuple[int, int, int]]()
        nums = sorted(nums)
        seen = set[int]()

        i, j, k = 0, 1, len(nums) - 1

        while i < j < k:
            if nums[i] > 0:
                break

            if i > 0 and nums[i] == nums[i - 1]:
                continue

            while j < k:
                if (-nums[i]) < (nums[j] + nums[k]):
                    k -= 1
                elif (-nums[i]) > (nums[j] + nums[k]):
                    j += 1
                else:
                    valid_sums.add((nums[i], nums[j], nums[k]))
                    j += 1

            seen.add(nums[i])
            while nums[i] in seen and i < len(nums) - 2:
                i += 1

            j = i + 1
            k = len(nums) - 1

        return [[a, b, c] for a, b, c in valid_sums]
