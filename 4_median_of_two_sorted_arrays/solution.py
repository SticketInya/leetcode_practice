from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # This is one of the worst and most unintuitive problems out there
        if len(nums1) < len(nums2):
            a, b = nums1, nums2
        else:
            a, b = nums2, nums1

        left, right = 0, len(a) - 1
        total = len(nums1) + len(nums2)
        half = total // 2

        while True:
            i = (left + right) // 2
            j = half - i - 2

            a_left = a[i] if i >= 0 else float("-infinity")
            a_right = a[i + 1] if i + 1 < len(a) else float("infinity")
            b_left = b[j] if j >= 0 else float("-infinity")
            b_right = b[j + 1] if j + 1 < len(b) else float("infinity")

            if a_left <= b_right and b_left <= a_right:
                if total % 2 == 1:
                    return min(a_right, b_right)
                else:
                    return (min(a_right, b_right) + max(a_left, b_left)) / 2
            elif a_left > b_right:
                right = i - 1
            else:
                left = i + 1
