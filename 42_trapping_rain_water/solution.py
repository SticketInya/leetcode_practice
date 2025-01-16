from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) <= 2:
            return 0

        total_water = 0
        prefix_max = [0] * len(height)
        postfix_max = [0] * len(height)
        for i in range(1, len(height), 1):
            prefix_max[i] = max(height[i - 1], prefix_max[i - 1])

        for i in range(len(height) - 2, -1, -1):
            postfix_max[i] = max(height[i + 1], postfix_max[i + 1])

        for i in range(len(height) - 1):
            total_water += max(min(postfix_max[i], prefix_max[i]) - height[i], 0)

        return total_water

    def trapTwoPointers(self, height: List[int]) -> int:
        if len(height) <= 2:
            return 0

        leftMax, rightMax = height[0], height[-1]
        left, right = 0, len(height) - 1
        total_water = 0
        while left < right:
            if rightMax < leftMax:
                right -= 1
                rightMax = max(rightMax, height[right])
                total_water += rightMax - height[right]
            else:
                left += 1
                leftMax = max(leftMax, height[left])
                total_water += leftMax - height[left]

        return total_water
