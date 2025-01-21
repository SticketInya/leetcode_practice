from typing import Dict, List, Tuple


class TimeMap:

    def __init__(self):
        self.__map: Dict[str, List[Tuple[int, str]]] = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.__map:
            self.__map[key] = []
        self.__map[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        nums = self.__map.get(key, [])
        if not nums:
            return ""

        left, right = 0, len(nums) - 1
        current_max = nums[0]

        while left <= right:
            mid = (left + right) // 2

            if nums[mid][0] == timestamp:
                return nums[mid][1]

            if nums[mid][0] > timestamp:
                right = mid - 1
            else:
                if nums[mid][0] > current_max[0]:
                    current_max = nums[mid]
                left = mid + 1

        return current_max[1] if timestamp > current_max[0] else ""


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
