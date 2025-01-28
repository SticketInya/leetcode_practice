class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        def get_index(s: str) -> int:
            return ord(s) - ord("a")

        k = len(s1)
        target = [0] * 26
        window = [0] * 26
        for i in range(k):
            window[get_index(s2[i])] += 1
            target[get_index(s1[i])] += 1

        if window == target:
            return True

        left = 0
        for right in range(k, len(s2), 1):
            window[get_index(s2[left])] -= 1
            window[get_index(s2[right])] += 1
            left += 1

            if window == target:
                return True

        return False
