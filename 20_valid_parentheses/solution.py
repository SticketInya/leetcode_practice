from typing import List, Union


class Solution:
    closing_map = {"}": "{", "]": "[", ")": "("}
    opening_brackets = ["[", "{", "("]

    def is_valid_stack(self, s: str) -> bool:
        """
        The plain list solution is more intuitive and simpler
        but I wanted to write a simple stack for demonstration
        purposes
        """

        class ParenthesesStack:
            items: List[str] = []

            def add_item(self, item: str) -> None:
                self.items.append(item)

            def get_item(self) -> Union[str, None]:
                return None if not len(self.items) else self.items[len(self.items) - 1]

            def remove_item(self) -> None:
                if len(self.items):
                    self.items.pop()

        brackets = ParenthesesStack()

        for bracket in s:
            if bracket in self.opening_brackets:
                brackets.add_item(bracket)
                continue

            top_bracket = brackets.get_item()
            if not top_bracket:
                return False

            if self.closing_map.get(bracket) != top_bracket:
                return False
            brackets.remove_item()

        return brackets.get_item() is None

    def is_valid(self, s: str) -> bool:
        brackets: List[str] = []

        for bracket in s:
            if bracket in self.opening_brackets:
                brackets.append(bracket)
                continue
            if not len(brackets):
                return False
            if self.closing_map.get(bracket) != brackets[len(brackets) - 1]:
                return False
            brackets.pop()

        return len(brackets) == 0
