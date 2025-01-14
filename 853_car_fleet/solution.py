from typing import List


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = sorted(
            [(position[i], speed[i]) for i in range(len(position))], reverse=True
        )

        stack = []
        for p in pairs:
            time = (target - p[0]) / p[1]

            if not stack:
                stack.append(time)
                continue

            if time > stack[-1]:
                stack.append(time)

        return len(stack)
