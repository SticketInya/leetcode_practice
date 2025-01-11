from collections import defaultdict
from typing import Dict, List


class Solution:
    def top_frequent_k(self, nums: List[int], k: int) -> List[int]:
        frequency_map: Dict[int, int] = defaultdict(int)
        for num in nums:
            frequency_map[num] += 1

        return [
            key
            for key, _ in sorted(
                frequency_map.items(), key=lambda x: x[1], reverse=True
            )[:k]
        ]

    def top_k_with_bucket_sort(self, nums: List[int], k: int) -> List[int]:
        frequency_map: Dict[int, int] = defaultdict(int)
        for num in nums:
            frequency_map[num] += 1

        frequencies: List[List[int]] = [[] for _ in range(len(nums) + 1)]
        for num, count in frequency_map.items():
            frequencies[count].append(num)

        top_k: List[int] = []
        for i in range(len(frequencies) - 1, 0, -1):
            for num in frequencies[i]:
                top_k.append(num)
                if len(top_k) == k:
                    return top_k

        return []
