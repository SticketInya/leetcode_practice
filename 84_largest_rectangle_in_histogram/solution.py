from typing import List, Tuple


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        if len(heights) == 1:
            return heights[0]

        max_area = 0
        stack: List[Tuple[int, int]] = []
        for i in range(len(heights)):
            if not stack or stack[-1][1] <= heights[i]:
                stack.append((i, heights[i]))
                continue

            popped_width = 0
            while stack and stack[-1][1] > heights[i]:
                start, height = stack.pop()
                width = i - start
                max_area = max(max_area, height * width)
                popped_width = width

            stack.append((i - popped_width, heights[i]))

        while stack:
            start, height = stack.pop()
            max_area = max(max_area, height * (len(heights) - start))

        return max_area
