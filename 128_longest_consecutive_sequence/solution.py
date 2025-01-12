from typing import List


class Solution:
    def longest_consecutive(self, nums: List[int]) -> int:
        unique_values = set(nums)
        visited = set[int]()
        longest = 0

        # A youtube commenter pointed out that in case there are
        # a lot of repeating values, walking through the set
        # provides a better runtime while not impacting regular
        # test cases
        for num in unique_values:
            if num in visited:
                continue
            is_start_of_set = num - 1 not in unique_values
            if not is_start_of_set:
                continue

            next_value = num + 1
            streak = 1
            while next_value in unique_values:
                visited.add(next_value)
                streak += 1
                next_value += 1

            longest = max(longest, streak)

            # The exit condition and the visited set is leetcode
            # specific. While th solution with and without them is O(n)
            # the leetcode code executor kept timing out. I did not
            # experience the same timeout issue with other platforms, such as neetcode
            if longest > len(nums) // 2:
                break

        return longest
