import re


class Solution:
    def isPalindrome(self, s: str) -> bool:
        if s.strip() == "":
            return True

        clean_s = re.findall("[a-z0-9]", s.lower())
        return "".join(clean_s) == "".join(clean_s[::-1])

    def isPalindromeTwoPointers(self, s: str) -> bool:
        def isAlphaNumeric(s: str) -> bool:
            # Regex usage here would be fine
            # but it is much slower
            return (
                (ord("A") <= ord(s) <= ord("Z"))
                or (ord("a") <= ord(s) <= ord("z"))
                or (ord("0") <= ord(s) <= ord("9"))
            )

        s = s.lower()
        left, right = 0, len(s) - 1

        while left < right:
            while left < right and not isAlphaNumeric(s[left]):
                left += 1
            while left < right and not isAlphaNumeric(s[right]):
                right -= 1

            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1

        return True
