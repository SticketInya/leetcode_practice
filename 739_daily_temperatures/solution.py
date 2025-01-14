from typing import List, Tuple


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        days = [0] * len(temperatures)
        stack: List[Tuple[int, int]] = []

        for i in range(len(temperatures) - 1, -1, -1):

            while stack and temperatures[i] >= stack[-1][0]:
                stack.pop()

            if stack:
                days[i] = stack[-1][1] - i

            stack.append((temperatures[i], i))

        return days

    def dailyTemperatures2(self, temperatures: List[int]) -> List[int]:
        days = [0] * len(temperatures)
        stack: List[Tuple[int, int]] = []

        for i in range(len(temperatures)):
            while stack and stack[-1][0] < temperatures[i]:
                removed = stack.pop()
                days[removed[1]] = i - removed[1]

            stack.append((temperatures[i], i))

        return days
