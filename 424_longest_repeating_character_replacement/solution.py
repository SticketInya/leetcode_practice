class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        chars = set[str](s)
        longest = 0

        for c in chars:
            left = 0
            count_unique = 0
            for right in range(len(s)):
                if s[right] != c:
                    count_unique += 1

                while count_unique > k:
                    if s[left] != c:
                        count_unique -= 1
                    left += 1

                length = right - left + 1
                longest = max(length, longest)

        return longest

    def characterReplacementOptimized(self, s: str, k: int) -> int:
        chars = {}
        longest = 0

        left = 0
        max_frequency = 0
        for right in range(len(s)):
            chars[s[right]] = chars.get(s[right], 0) + 1
            max_frequency = max(max_frequency, chars[s[right]])

            while (right - left + 1) - max_frequency > k:
                chars[s[left]] -= 1
                left += 1

            length = right - left + 1
            longest = max(length, longest)

        return longest
