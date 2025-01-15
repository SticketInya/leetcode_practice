import re


class Solution:
    def isPalindrome(self, s: str) -> bool:
        if s.strip() == "":
            return True

        clean_s = re.findall("[a-z0-9]", s.lower())
        return "".join(clean_s) == "".join(clean_s[::-1])
