from typing import Dict


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        longest = 1
        left = 0
        chars = set[str](s[0])

        for right in range(1, len(s), 1):
            while s[right] in chars:
                chars.remove(s[left])
                left += 1

            chars.add(s[right])
            longest = max(longest, len(chars))

        return longest
