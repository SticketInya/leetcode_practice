from collections import defaultdict
from typing import Dict, List


class Solution:
    def top_frequent_k(self, nums: List[int], k: int) -> List[int]:
        frequency_map: Dict[int, int] = defaultdict(int)
        for num in nums:
            frequency_map[num] += 1

        print(frequency_map)
        print(sorted(frequency_map))
        print(sorted(frequency_map.items(), key=lambda x: x[1]))
        return [
            key
            for key, _ in sorted(
                frequency_map.items(), key=lambda x: x[1], reverse=True
            )[:k]
        ]
