from typing import List


class MinStack:

    def __init__(self):
        self.__min_values: List[int] = []
        self.__values: List[int] = []

    def push(self, val: int) -> None:
        self.__values.append(val)
        if not len(self.__min_values):
            self.__min_values.append(val)
        elif self.__min_values[-1] >= val:
            self.__min_values.append(val)

    def pop(self) -> None:
        current_val = self.__values.pop()
        if self.__min_values[-1] == current_val:
            self.__min_values.pop()

    def top(self) -> int:
        return self.__values[-1]

    def get_min(self) -> int:
        return self.__min_values[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
